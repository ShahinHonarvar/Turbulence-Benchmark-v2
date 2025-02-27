def all_left_right_truncatable_prime(args_tuple):
    x = args_tuple[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or n < 13:
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i + 1:])):
                return False
        return True
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and is_left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    truncatable_primes.sort()
    return truncatable_primes