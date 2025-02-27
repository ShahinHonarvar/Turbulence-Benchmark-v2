from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[945]
    result = []
    for num in range(1, x + 1):
        if isprime(num) and (not any((int(digit) == 0 for digit in str(num)))):
            is_ltrunc = True
            is_rtrunc = True
            while len(str(num)) > 1:
                num = int(str(num)[1:]) if is_ltrunc else int(str(num)[:-1])
                if not isprime(num) or any((int(digit) == 0 for digit in str(num))):
                    is_ltrunc = False
                    is_rtrunc = False
                    break
            if is_ltrunc and is_rtrunc:
                result.append(num)
    return sorted(result, reverse=True)