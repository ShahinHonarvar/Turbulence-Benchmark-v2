from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[26]
    result = []
    for num in range(2, x + 1):
        if isprime(num):
            is_ltruncatable = all((isprime(int(str(num)[i:])) for i in range(1, len(str(num)))))
            is_rtruncatable = all((isprime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1)))
            if is_ltruncatable and is_rtruncatable:
                result.append(num)
    return sorted(result)