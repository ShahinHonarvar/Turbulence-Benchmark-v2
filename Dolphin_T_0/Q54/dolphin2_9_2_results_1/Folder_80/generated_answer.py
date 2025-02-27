def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 2:
            return False
        if n < 10:
            return True
        if n % 10 == 0:
            return False
        while n > 9:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[14]
    primes = [i for i in range(2, x) if is_right_truncatable(i) and is_prime(i)]
    return sorted(primes, reverse=True)