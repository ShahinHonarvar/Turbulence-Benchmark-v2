def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            left = int(n[:i + 1])
            right = int(n[i:])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    truncatable_primes = []
    for n in range(1, x + 1):
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)