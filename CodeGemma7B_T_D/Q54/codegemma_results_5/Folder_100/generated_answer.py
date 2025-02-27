def all_right_truncatable_prime(t: tuple[int, ...]) -> list[int]:
    x = t[26]
    ntrp = set()
    for p in range(10 ** (len(str(x)) - 1), x):
        sum_to_test = p
        digit_to_test = p
        while digit_to_test >= 10:
            digit_to_test = digit_to_test // 10
            sum_to_test -= digit_to_test
            if not is_prime(sum_to_test):
                break
        if is_prime(p) and is_prime(sum_to_test):
            ntrp.add(p)
    return sorted(ntrp)

def is_prime(p: int) -> bool:
    if p <= 1:
        return False
    elif p <= 3:
        return True
    elif p % 2 == 0 or p % 3 == 0:
        return False
    else:
        i = 5
        limit = int(p ** 0.5) + 1
        while i < limit:
            if p % i == 0 or p % (i + 2) == 0:
                return False
            i += 6
        return True