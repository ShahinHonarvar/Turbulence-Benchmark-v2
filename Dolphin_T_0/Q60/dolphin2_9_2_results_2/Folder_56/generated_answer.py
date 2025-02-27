def all_left_right_truncatable_prime(numbers):
    check_prime = lambda num: all((num % i for i in range(2, int(num ** 0.5) + 1)))

    def check_truncatable(n):
        if '0' in str(n):
            return False
        while n > 9:
            n = n % 10 ** (len(str(n)) - 1)
            if n < 10 and n not in [2, 3, 5, 7] or not check_prime(n):
                return False
        return True
    x = numbers[30]
    primes = [n for n in range(2, x + 1) if check_prime(n) and check_truncatable(n)]
    return primes