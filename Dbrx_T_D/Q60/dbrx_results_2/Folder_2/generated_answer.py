from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[618]
    result = []
    for num in range(1, x + 1):
        if not isprime(num):
            continue
        digits = str(num)
        for i in range(len(digits) - 1):
            if not isprime(int(digits[i:])):
                break
        else:
            for j in range(len(digits)):
                if not isprime(int(digits[:j])):
                    break
            else:
                result.append(num)
    return sorted(list(set(result)))