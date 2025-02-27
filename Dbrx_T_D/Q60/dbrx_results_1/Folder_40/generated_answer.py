from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[10]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and (not any((c == '0' for c in str(num)))):
            is_truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)