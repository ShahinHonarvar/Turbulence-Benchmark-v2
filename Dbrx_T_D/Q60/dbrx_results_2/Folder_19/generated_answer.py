from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[67]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result, reverse=True)