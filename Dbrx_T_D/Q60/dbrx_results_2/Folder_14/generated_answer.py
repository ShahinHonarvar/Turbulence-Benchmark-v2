from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):
    x = max(input_tuple[77], 2)
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
        n = int(str(n)[:-1])
        if not isprime(n):
            return False
    return True