def is_left_truncatable_prime(n):

    def is_not_contains_0(n):
        return '0' not in str(n)

    def is_not_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if not is_not_contains_0(n):
        return False
    for i in range(len(str(n)) - 1, 0, -1):
        n = int(str(n)[i:])
        if not is_not_prime(n):
            return False
    return True

def all_left_truncatable_prime(s):
    x = list(s)[992]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return left_truncatable_primes