def all_right_truncatable_prime(numbers):

    def check_truncatable(n):
        while n:
            if n == 2 or n == 3 or n == 5 or (n == 7):
                return True
            last_digit = n % 10
            n //= 10
            if last_digit not in [2, 3, 5, 7] or n % last_digit == 0:
                return False
        return True

    def check_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = numbers[24]
    primes = [i for i in range(2, x) if check_prime(i)]
    right_truncatable_prime = [i for i in primes if check_truncatable(i)]
    return sorted(right_truncatable_prime)