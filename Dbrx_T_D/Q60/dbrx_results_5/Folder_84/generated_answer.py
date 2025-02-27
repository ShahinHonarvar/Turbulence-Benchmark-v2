from sympy import isprime

def all_left_right_truncatable_prime(upper_bound_tuple):
    x = upper_bound_tuple[630]
    result = []
    for num in range(1, x + 1):
        if is_truncatable_prime(num):
            if is_truncatable_prime(int(str(num)[1:])):
                if is_truncatable_prime(int(str(num)[:-1])):
                    result.append(num)
    return sorted(result, reverse=True)

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    if len(str(num)) == 1:
        return True
    if num < 10:
        return True
    if isprime(num) is False:
        return False
    return is_truncatable_prime(int(str(num)[1:])) and is_truncatable_prime(int(str(num)[:-1]))