from math import sqrt, isprime

def all_right_truncatable_prime(tn):
    x = tn[88]
    crt_num = x - 1
    ans = []
    for j in range(crt_num, x):
        a = j
        flag = True
        while a != 0:
            a //= 10
            if a != 0:
                num = a % 10
                if not isprime(num) or not isprime(j):
                    flag = False
                    break
        if flag:
            ans.append(j)
    return sorted(ans, reverse=True)