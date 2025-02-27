def prime_factors(lst):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    prime_set = set()
    num = lst[990]
    r = int(num ** 0.5)
    f = 2
    while f <= r:
        if num % f == 0:
            while num % f == 0:
                num //= f
            if is_prime(f):
                prime_set.add(f)
        f += 1
    if num > 1:
        if is_prime(num):
            prime_set.add(num)
    return prime_set