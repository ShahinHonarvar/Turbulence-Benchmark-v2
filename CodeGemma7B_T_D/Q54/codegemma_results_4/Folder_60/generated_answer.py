from math import sqrt

def all_right_truncatable_prime(n):
    x = n[87]
    s = []

    def isprime(y):
        if y < 2:
            return False
        elif y < 4:
            return True
        elif y % 2 == 0:
            return False
        k = 3
        while k <= sqrt(y):
            if y % k == 0:
                return False
            k += 2
        return True

    def gen(nu):
        nu = str(nu)
        for i in range(len(nu) - 1):
            if not isprime(int(nu[0:len(nu) - i] or nu[:-i - 1])):
                return
            s.append(int(nu[0:len(nu) - i] or nu[:-i - 1]))
    for i in range(2, x):
        if isprime(i):
            gen(i)
    return sorted(s)