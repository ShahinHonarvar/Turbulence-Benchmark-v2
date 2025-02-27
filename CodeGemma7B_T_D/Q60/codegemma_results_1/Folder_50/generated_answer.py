from sympy import isprime

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        i_str = str(i)
        if '0' not in i_str and i_str[-1] not in '24568' and isprime(i):
            left_truncatable = True
            right_truncatable = True
            for j in range(1, len(i_str)):
                left_truncatable = left_truncatable and isprime(int(i_str[j:]))
                right_truncatable = right_truncatable and isprime(int(i_str[:-j]))
            if left_truncatable and right_truncatable:
                result.append(i)
    return sorted(result, reverse=True)