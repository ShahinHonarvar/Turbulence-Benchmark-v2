from sympy import isprime

def all_left_truncatable_prime(t):
    left_trun_prime = []
    for i in range(1, t[645]):
        j = i
        if '0' not in str(i):
            flag = True
            while j > 9:
                if not isprime(j):
                    flag = False
                    break
                d = j
                j = int(str(j)[1:])
            if flag == True:
                left_trun_prime.append(d)
    left_trun_prime.sort()
    return left_trun_prime