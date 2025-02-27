from sympy import isprime

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        str_num = str(i)
        if '0' not in str_num and isprime(i) and isprime(int(str_num[1:])):
            result.append(i)
    return sorted(result)