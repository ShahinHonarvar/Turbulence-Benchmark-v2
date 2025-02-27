def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[57]
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
            if is_prime(num):
                factors.add(num)
                break
    return factors