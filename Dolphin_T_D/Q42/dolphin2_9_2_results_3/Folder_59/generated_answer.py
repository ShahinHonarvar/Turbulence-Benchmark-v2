def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif n < 9:
            return True
        elif n % 3 == 0:
            return False
        else:
            r = int(n ** 0.5)
            f = 5
            while f <= r:
                if n % f == 0:
                    return False
                if n % (f + 2) == 0:
                    return False
                f += 6
            return True
    prime_factors_set = set()
    for num in numbers[2:]:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                if is_prime(i):
                    prime_factors_set.add(i)
    return prime_factors_set