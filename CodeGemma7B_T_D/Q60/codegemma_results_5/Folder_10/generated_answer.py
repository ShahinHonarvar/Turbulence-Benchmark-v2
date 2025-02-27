from sympy import isprime

def all_left_right_truncatable_prime(n):
    result = []
    for p in range(2, n + 1):
        if isprime(p):
            str_p = str(p)
            if '0' not in str_p:
                new_p = int(str_p[1:len(str_p)])
                if new_p > 1 and isprime(new_p):
                    new_p = int(str_p[0:len(str_p) - 1])
                    if new_p > 1 and isprime(new_p):
                        result.append(p)
    return sorted(result)[::-1]