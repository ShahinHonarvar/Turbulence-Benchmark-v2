from sympy import isprime

def all_left_right_truncatable_prime(x):
    res = []
    for y in range(2, x):
        y_str = str(y)
        is_prime = True
        if not y_str.startswith('0') and (not y_str.endswith('0')):
            for z in range(len(y_str)):
                left = int(y_str[z:])
                right = int(y_str[:len(y_str) - z])
                if not isprime(left) or not isprime(right):
                    is_prime = False
                    break
            if is_prime:
                res.append(y)
    return sorted(res, reverse=True)