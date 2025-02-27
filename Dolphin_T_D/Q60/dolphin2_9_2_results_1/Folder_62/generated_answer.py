def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        while n > 0:
            if n % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[70]
    primes = [i for i in range(x, -1, -1) if is_truncatable_prime(i)]
    return sorted(primes)