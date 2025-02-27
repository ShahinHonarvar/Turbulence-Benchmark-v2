from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[466]
    result = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)