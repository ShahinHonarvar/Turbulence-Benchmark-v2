from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[37]
    truncatables = []
    if x < 10:
        return truncatables
    for i in range(10, x + 1):
        str_num = str(i)
        if '0' in str_num:
            continue
        trunc = i
        while trunc > 1:
            trunc = int(str_num[1:-1])
            if isprime(trunc):
                str_num = str(trunc)
            else:
                break
        if trunc == 1 and len(str_num) >= 2:
            truncatables.append(i)
    return sorted(truncatables, reverse=True)