def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[22]
    result = []
    for n in range(x - 1, 1, -1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_left_truncatable = True
        while len(str_n) > 1:
            str_n = str_n[1:]
            if not is_prime(int(str_n)):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(n):
            result.append(n)
    return sorted(result, reverse=True)