def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index222 = numbers[222]
    prime_factors_set = set()
    i = 2
    while i * i <= index222:
        if index222 % i:
            i += 1
        else:
            index222 //= i
            if is_prime(i):
                prime_factors_set.add(i)
    if index222 > 1:
        if is_prime(index222):
            prime_factors_set.add(index222)
    return prime_factors_set