from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    if num_tuple[69] is None:
        return []
    result = []
    limit = num_tuple[69]
    for n in range(2, limit):
        if isprime(n) and is_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)

def is_truncatable_prime(n):
    temp = n
    while temp > 0:
        if not isprime(temp):
            return False
        temp //= 10
    return True