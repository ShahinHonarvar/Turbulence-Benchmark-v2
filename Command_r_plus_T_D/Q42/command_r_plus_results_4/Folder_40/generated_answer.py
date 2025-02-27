def prime_factors(numbers_list):

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
    seventh_number = numbers_list[7]
    factors = set()
    for i in range(2, seventh_number + 1):
        while seventh_number % i == 0:
            factors.add(i)
            seventh_number //= i
        if seventh_number == 1:
            break
    factors = {factor for factor in factors if is_prime(factor)}
    return factors