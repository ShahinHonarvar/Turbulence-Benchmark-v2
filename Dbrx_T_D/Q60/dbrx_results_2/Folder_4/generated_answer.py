from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[96]
    result = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        digits = len(str(num))
        flag = True
        for i in range(1, digits):
            if not isprime(int(str(num)[i:])):
                flag = False
                break
        if not flag:
            continue
        for i in range(digits - 1, 0, -1):
            if not isprime(int(str(num)[:i])):
                flag = False
                break
        if flag:
            result.append(num)
    return sorted(result, reverse=True)