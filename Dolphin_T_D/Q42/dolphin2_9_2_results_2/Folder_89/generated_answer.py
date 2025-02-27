def prime_factors(lst):

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
    num = lst[18]
    result = set()
    i = 2
    while i * i <= num:
        if num % i == 0 and is_prime(i):
            result.add(i)
        i += 1
    return result