from sympy import isprime

def all_left_right_truncatable_prime(bound_tuple):
    x = bound_tuple[85]
    ltp = [i for i in range(2, x + 1) if isprime(i)]
    lrtp = []
    for num in ltp:
        if '0' in str(num):
            continue
        digits = len(str(num))
        for i in range(1, digits):
            if not isprime(int(str(num)[i:])):
                break
            if not isprime(int(str(num)[:-i])):
                break
        else:
            lrtp.append(num)
    return sorted(lrtp)