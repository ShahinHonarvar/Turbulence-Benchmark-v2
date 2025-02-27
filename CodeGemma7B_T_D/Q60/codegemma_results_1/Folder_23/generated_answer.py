from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[77]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if isprime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not isprime(int(str_i[j:])):
                    break
                if not isprime(int(str_i[:-j])):
                    break
            else:
                result.append(i)
    result.sort(reverse=True)
    return result