from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[767]
    result = []
    for i in range(x, 0, -1):
        if isprime(i) and '0' not in str(i):
            temp = i
            while temp > 1:
                if not isprime(temp):
                    break
                temp //= 10
            if temp == 1:
                result.append(i)
    return sorted(result, reverse=True)