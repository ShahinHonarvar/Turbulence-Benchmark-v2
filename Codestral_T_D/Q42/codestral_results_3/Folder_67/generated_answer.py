def prime_factors(num_list):

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
    num = num_list[43]
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            if is_prime(i):
                factors.add(i)
    if num > 1 and is_prime(num):
        factors.add(num)
    return factors