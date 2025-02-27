from sympy import isprime

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' not in str_i and isprime(i):
            for j in range(len(str_i) - 2):
                if not isprime(int(str_i[j + 1:])):
                    break
                if j == len(str_i) - 3:
                    result.append(i)
    return sorted(result)