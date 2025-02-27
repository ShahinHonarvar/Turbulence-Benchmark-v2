from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = list(numbers_tuple)[91]
    left_right_truncatables = []
    for num in range(1, x + 1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatables.append(num)
    return sorted(left_right_truncatables)

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    num_str = str(n)
    for i in range(1, len(num_str)):
        if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
            return False
    return True