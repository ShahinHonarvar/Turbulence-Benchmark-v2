def all_right_truncatable_prime(t):
    x = t[39]

    def check_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and check_truncatable(n // 10)
    prime_numbers = [i for i in range(2, x) if is_prime(i) and check_truncatable(i)]
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n in {0, 1}:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True