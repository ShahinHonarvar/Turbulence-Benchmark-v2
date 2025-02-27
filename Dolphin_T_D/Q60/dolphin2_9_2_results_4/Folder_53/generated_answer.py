def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[86]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and is_prime(int(str(i)[1:-1])):
            result.append(i)
    return list(reversed(result))