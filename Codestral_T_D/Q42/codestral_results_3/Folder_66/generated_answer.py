def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    factors = set()
    num = numbers[42]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            if is_prime(i):
                factors.add(i)
            num //= i
    if num > 1 and is_prime(num):
        factors.add(num)
    return factors