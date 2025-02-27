from sympy import isprime

def all_left_truncatable_prime(x):
    result = []
    for i in range(1, x):
        if '0' not in str(i) and isprime(i):
            temp = str(i)
            for j in range(1, len(temp)):
                if not isprime(int(temp[j:])):
                    break
            else:
                result.append(i)
    return sorted(result)