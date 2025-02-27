def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        while i > 1:
            if not is_prime(i):
                break
            i = i // 10
        else:
            result.append(i)
    return sorted(result)