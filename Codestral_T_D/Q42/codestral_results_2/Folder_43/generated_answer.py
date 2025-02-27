def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    factors = set()
    num = num_list[29]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0 and is_prime(i):
            factors.add(i)
            num = num / i
    if num > 1 and is_prime(num):
        factors.add(int(num))
    return factors