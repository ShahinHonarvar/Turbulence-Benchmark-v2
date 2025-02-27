from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[57]
    ltp = []
    for i in range(2, x):
        if isprime(i):
            flag = True
            for j in str(i):
                if j == '0' or not isprime(int(str(i)[1:])):
                    flag = False
                    break
            if flag:
                ltp.append(i)
    return sorted(ltp, reverse=True)