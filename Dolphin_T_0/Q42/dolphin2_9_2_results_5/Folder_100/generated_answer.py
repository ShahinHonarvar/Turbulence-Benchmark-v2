def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def prime_factors(lst):

    def is_prime(n):
        if n < 2:
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
    number = lst[99]
    while number != 1:
        i = 2
        while i <= number:
            if gcd(number, i) > 1 and is_prime(i):
                factors.add(i)
                number = number / i
            else:
                i += 1
    return factors