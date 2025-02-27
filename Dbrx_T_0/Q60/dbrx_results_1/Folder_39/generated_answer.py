from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[30]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            is_ltruncatable = True
            is_rtruncatable = True
            while num > 9:
                num = int(str(num)[1:]) if is_ltruncatable else int(str(num)[:-1])
                if not isprime(num):
                    is_ltruncatable = False
                    is_rtruncatable = False
                    break
            if is_ltruncatable and is_rtruncatable:
                result.append(num)
    return sorted(result, reverse=True)