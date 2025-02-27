from sympy import isprime

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[758]
    result = []
    for num in range(1, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    if '0' in str(num) or not isprime(num):
        return False
    while len(str(num)) > 1:
        num = int(str(num)[1:]) if str(num)[0] == '1' else int(str(num)[1:])
        if not isprime(num):
            return False
    return True