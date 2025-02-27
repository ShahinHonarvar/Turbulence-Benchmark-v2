from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[18]
    rtn = []
    for i in range(1, 10):
        if isprime(i):
            tmp = 10 * i + 1
            while tmp < x:
                if isprime(tmp):
                    rtn.append(tmp)
                    tmp = 10 * tmp + 1
                else:
                    break
    for i in range(2, 10):
        if isprime(i):
            tmp = i
            while tmp < x:
                if isprime(tmp):
                    rtn.append(tmp)
                    tmp = 10 * tmp + i
                else:
                    break
    rtn.sort(reverse=True)
    return rtn