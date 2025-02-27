def all_left_truncatable_prime(x):

    def is_left_truncatable(n):
        b = [c for c in str(n)]
        while b and all(map(int, b)):
            if not is_prime(int(''.join(map(str, b)))):
                return False
            b.pop(0)
        return True

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    left_truncatable_primes = [n for n in range(2, x) if is_prime(n) and is_left_truncatable(n)]
    return sorted(left_truncatable_primes)