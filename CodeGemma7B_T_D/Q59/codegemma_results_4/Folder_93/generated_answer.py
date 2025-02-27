from sympy import isprime

def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(number):
        str_number = str(number)
        if '0' in str_number:
            return False
        for i in range(1, len(str_number)):
            candidate = int(str_number[i:])
            if not isprime(candidate):
                return False
        return True
    x = t[11]
    result = []
    for i in range(2, x):
        if isprime(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)