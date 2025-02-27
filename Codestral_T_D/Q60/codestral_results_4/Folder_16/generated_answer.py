def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    truncable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            truncable_primes.append(num)
    return truncable_primes