import sympy

def all_left_right_truncatable_prime(values):

    def is_truncatable(prime):
        str_p = str(prime)
        if '0' in str_p:
            return False
        for i in range(1, len(str_p)):
            if not sympy.isprime(int(str_p[i:])) or not sympy.isprime(int(str_p[:-i])):
                return False
        return True
    x = values[24]
    results = []
    for num in range(11, x + 1):
        if sympy.isprime(num) and is_truncatable(num):
            results.append(num)
    return results