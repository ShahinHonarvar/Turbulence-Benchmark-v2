from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[31]
    result = []
    for i in range(1, x):
        if isprime(i):
            flag = True
            for j in str(i):
                if j == '0' or not isprime(int(str(i)[1:])):
                    flag = False
                    break
            if flag:
                result.append(i)
    result.sort(reverse=True)
    return result