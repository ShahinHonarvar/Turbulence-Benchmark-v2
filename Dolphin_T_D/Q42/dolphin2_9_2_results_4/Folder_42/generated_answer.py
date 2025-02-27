def prime_factors(lst):
    num = lst[276]
    result = set()

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            result.add(i)
            result.add(num // i)
    return result