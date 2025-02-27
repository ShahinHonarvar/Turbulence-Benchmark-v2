def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        if n % 3 == 0 or n % 5 == 0:
            return False
        if n % 17 == 0 or n % 7 == 0:
            return False
        if n % 19 == 0 or n % 23 == 0:
            return False
        if n % 41 == 0 or n % 29 == 0:
            return False
        if n % 43 == 0 or n % 47 == 0:
            return False
        if n % 53 == 0 or n % 73 == 0:
            return False
        if n % 83 == 0 or n % 79 == 0:
            return False
        return True

    def prime_factors_of_a_number(n):
        prime_factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if is_prime(i):
                    prime_factors.add(i)
        if n > 1 and is_prime(n):
            prime_factors.add(n)
        return prime_factors
    return prime_factors_of_a_number(numbers[733])