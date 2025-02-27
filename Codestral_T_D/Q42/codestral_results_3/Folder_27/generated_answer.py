def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = lst[56]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
            if is_prime(num):
                factors.add(num)
                break
    if num > 1:
        factors.add(num)
    return factors