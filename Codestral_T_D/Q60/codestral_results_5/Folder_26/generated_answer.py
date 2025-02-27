def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def truncated_primes(n):
        if n < 10:
            return is_prime(n)
        for i in range(1, len(str(n))):
            if not (is_prime(int(str(n)[:-i])) and is_prime(int(str(n)[i:]))):
                return False
        return True
    x = t[81]
    return sorted(filter(truncated_primes, range(2, x + 1)), reverse=True)