def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t, x=t[32]):
    if all((is_prime(int(str(x)[i:j + 1])) for i in range(len(str(x))) for j in range(i, len(str(x))))):
        return [x]
    return []