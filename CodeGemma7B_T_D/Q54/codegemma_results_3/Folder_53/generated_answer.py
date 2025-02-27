from sympy import isprime

def all_right_truncatable_prime(tp):
    x = tp[86]
    result = []
    for i in range(2, x):
        if isprime(i):
            n = i
            temp = True
            while True:
                n = int(str(n)[:-1])
                if n == 0:
                    break
                if not isprime(n):
                    temp = False
                    break
            if temp:
                result.append(i)
    result.sort(reverse=True)
    return result