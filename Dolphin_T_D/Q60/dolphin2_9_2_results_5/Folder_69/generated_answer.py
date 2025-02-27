def is_prime(n):
    if n in (0, 1):
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_valid(n):
    if n in (0, 1):
        return False
    n_len = len(str(n))
    for i in range(n_len):
        for j in range(i + 1, n_len + 1):
            if not is_prime(int(str(n)[i:j])):
                return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[760]
    prime_set = set()
    for i in range(x, 0, -1):
        if is_prime(i) and is_valid(i):
            prime_set.add(i)
    return sorted(list(prime_set), reverse=True)