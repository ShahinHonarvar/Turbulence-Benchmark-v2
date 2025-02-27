def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for divisor in range(2, sqrt_n):
            if n % divisor == 0:
                return False
        return True
    x = numbers[74]
    primes = [2]
    if x < 2:
        return []
    for num in range(3, x):
        if is_prime(num):
            primes.append(num)
    left_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[i:])) for i in range(len(str(p)))))]
    return left_truncatable_primes