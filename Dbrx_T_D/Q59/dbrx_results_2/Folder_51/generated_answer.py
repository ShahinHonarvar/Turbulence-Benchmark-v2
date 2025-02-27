from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[54]
    result = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n < 10 and isprime(n):
        return True
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True