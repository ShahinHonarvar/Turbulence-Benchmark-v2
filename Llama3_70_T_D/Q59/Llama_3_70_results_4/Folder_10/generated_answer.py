def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = num_tuple[38]
    truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)