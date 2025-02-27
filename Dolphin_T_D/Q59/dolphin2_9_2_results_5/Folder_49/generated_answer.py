def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[14]
    primes = [i for i in range(x) if is_prime(i)]
    return sorted([p for p in primes if is_truncatable(p)])