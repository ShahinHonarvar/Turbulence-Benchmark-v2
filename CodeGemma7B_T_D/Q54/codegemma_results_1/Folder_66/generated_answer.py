from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[25]
    res = []
    for i in range(2, x):
        if isprime(i):
            digit = 1
            temp = i
            while temp >= 10 ** digit:
                temp = temp % 10 ** digit
                digit += 1
                if not isprime(temp):
                    break
            else:
                res.append(i)
    res.sort(reverse=True)
    return res