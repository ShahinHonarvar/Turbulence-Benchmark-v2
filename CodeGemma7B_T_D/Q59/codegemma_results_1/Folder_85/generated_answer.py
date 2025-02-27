from sympy import isprime

def all_left_truncatable_prime(num):
    lst = []
    num = num[94]
    for i in range(2, num):
        if str(i)[:2] not in ('04', '56'):
            flag = True
            for j in range(len(str(i)) - 1):
                temp = i
                for k in range(j):
                    temp //= 10
                    if not isprime(temp):
                        flag = False
                        break
                if flag:
                    lst.append(i)
    return sorted(lst)