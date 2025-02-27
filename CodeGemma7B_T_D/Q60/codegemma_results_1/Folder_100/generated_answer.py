from sympy.ntheory.primetest import isprime
    import sympy

def all_left_right_truncatable_prime(l):
    """
    docstring goes here
    """
    x = l[26]
    S = int(str(x)[0])
    L = [i for i in sympy.primerange(2, x) if str(i)[-1] != '0' and (str(i)[-1] == '2' or str(i)[-1] == '3' or str(i)[-1] == '5' or (str(i)[-1] == '7'))]
    for k in L:
        cnt = 0
        p = []
        while True:
            if isprime(k):
                cnt += 1
                p.append(k)
            digits = list(str(k))
            first = digits.pop(0)
            k = int(''.join(digits))
            if isprime(k):
                cnt += 1
            if cnt == 2:
                break
    if S == 2:
        return p
    else:
        return []