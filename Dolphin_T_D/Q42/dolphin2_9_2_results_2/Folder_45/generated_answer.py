def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def prime_factors_of_n(n):
        lst = []
        while n % 2 == 0:
            lst.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                lst.append(i)
                n //= i
            i += 2
        if n > 2:
            lst.append(n)
        return set(lst)
    return prime_factors_of_n(numbers[33])