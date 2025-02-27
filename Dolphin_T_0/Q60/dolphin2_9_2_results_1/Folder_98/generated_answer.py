def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(x):
        if x < 5:
            return x in (2, 3)
        if x % 10 == 0 or int(str(x)[-1]) == 0 or int(str(x)[0]) == 0:
            return False
        return is_prime(int(str(x)[1:-1])) and is_truncatable(int(str(x)[1:])) and is_truncatable(int(str(x)[:-1]))
    primes = [str(x) for x in range(int(numbers[8]) + 1) if is_prime(x) and is_truncatable(x)]
    primes.sort(reverse=True)
    return primes