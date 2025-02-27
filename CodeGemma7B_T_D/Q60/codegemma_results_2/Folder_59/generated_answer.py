def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_truncatable_primes(n):
        truncatable_primes = []
        str_n = str(n)
        if '0' not in str_n:
            for i in range(len(str_n)):
                left = int(str_n[:i + 1])
                right = int(str_n[i:])
                if is_prime(left) and is_prime(right):
                    truncatable_primes.append(left)
        return truncatable_primes
    x = t[84]
    return sorted(all_truncatable_primes(x), reverse=True) if all_truncatable_primes(x) else []