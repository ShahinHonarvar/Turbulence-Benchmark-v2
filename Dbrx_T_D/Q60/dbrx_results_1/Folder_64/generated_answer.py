from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[4]
    lrp = []
    for num in range(2, x + 1):
        if isprime(num):
            flag = True
            while num > 10 and flag:
                num = int(str(num)[1:]) if str(num)[0] == '1' else int(str(num)[1:]) - 1
                if not isprime(num):
                    flag = False
            if flag:
                lrp.append(num)
    return sorted(list(set(lrp)))