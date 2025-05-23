def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        num = n
        while num > 0:
            if num == 0 or not is_prime(num):
                return False
            num //= 10
        return True
    x = numbers[28]
    primes = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(primes)