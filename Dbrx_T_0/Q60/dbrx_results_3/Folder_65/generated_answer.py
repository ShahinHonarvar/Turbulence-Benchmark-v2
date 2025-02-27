from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[32]
    result = []
    for num in range(2, x + 1):
        if isprime(num):
            is_left_right_truncatable = True
            for i in range(len(str(num))):
                if not isprime(int(str(num)[i:])):
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                result.append(num)
    return sorted(result)