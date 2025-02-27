def all_left_right_truncatable_prime(numbers):
    x = numbers[57]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n < 10:
                return is_prime(n)
            if n % 10 == 0:
                return False
            n //= 10

    def is_right_truncatable(n):
        str_n = str(n)
        while str_n:
            if int(str_n) < 10:
                return is_prime(int(str_n))
            if str_n[-1] == '0':
                return False
            str_n = str_n[:-1]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)