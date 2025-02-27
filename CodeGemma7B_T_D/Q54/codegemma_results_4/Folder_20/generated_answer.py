import math

def all_right_truncatable_prime(a):
    p = a[100]
    lst = []

    def isprime(n):
        if n <= 1:
            return False
        i = 3
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 2
        return True
    for i in range(2, p):
        if isprime(i):
            n = str(i)[::-1]
            if isprime(int(n)):
                lst.append(i)
    return sorted(lst, reverse=True)