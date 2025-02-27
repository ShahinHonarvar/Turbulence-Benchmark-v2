from sympy import isprime, nextprime

def all_left_right_truncatable_prime(t):
    x = t[41]
    res = []
    for y in range(2, x // 2 + 1):
        if isprime(y) and '0' not in str(y):
            xx = y
            while xx in range(2, x // 2 + 1):
                xx = nextprime(xx)
                if isprime(xx) and int(str(y) + str(xx)) in range(2, x):
                    t = xx
                    while t < x and int(str(t) + str(xx)) in range(2, x):
                        t = nextprime(t)
                    if t >= x:
                        res.append(int(str(y) + str(xx)))
                xx = nextprime(xx)
    return res[::-1]