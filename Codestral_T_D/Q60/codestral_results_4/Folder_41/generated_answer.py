def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        while str_n != '':
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[46]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_left_truncatable(n) and is_right_truncatable(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)