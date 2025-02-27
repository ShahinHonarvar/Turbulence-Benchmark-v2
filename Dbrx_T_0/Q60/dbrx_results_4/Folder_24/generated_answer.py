from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[65]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            is_ltrunc = True
            is_rtrunc = True
            while num > 9 and is_ltrunc and is_rtrunc:
                num = int(str(num)[1:]) if is_ltrunc else num
                num = int(str(num)[:-1]) if is_rtrunc else num
                is_ltrunc = is_ltrunc and isprime(num)
                is_rtrunc = is_rtrunc and isprime(num)
            if is_ltrunc and is_rtrunc:
                result.append(num)
    return sorted(result, reverse=True)