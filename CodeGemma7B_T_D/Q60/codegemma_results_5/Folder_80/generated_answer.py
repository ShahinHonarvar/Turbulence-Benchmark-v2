from sympy import isprime

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        i_str = str(i)
        if '0' not in i_str and isprime(i):
            for j in range(1, len(i_str)):
                left = int(i_str[j:])
                right = int(i_str[:-j])
                if left >= 2 and left <= 11 and (right >= 2) and (right <= 11) and isprime(left) and isprime(right):
                    result.append(i)
                    break
    return sorted(result, reverse=True)