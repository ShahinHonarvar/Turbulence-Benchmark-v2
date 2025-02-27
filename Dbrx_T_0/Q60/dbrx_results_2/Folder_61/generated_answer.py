from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[3]
    result = []
    for num in range(10, x + 1):
        if isprime(num) and (not any((int(num / 10 ** i) % 10 == 0 for i in range(len(str(num)) - 1)))):
            is_left_right_truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                result.append(num)
    return sorted(result, reverse=True)