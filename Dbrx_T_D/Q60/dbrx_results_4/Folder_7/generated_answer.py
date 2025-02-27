from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[803]
    result = []
    for num in range(1, x + 1):
        if isprime(num) and num > 10:
            str_num = str(num)
            left_truncatable = [int(str_num[i:]) for i in range(1, len(str_num))]
            right_truncatable = [int(str_num[:i]) for i in range(1, len(str_num))]
            if all((isprime(i) for i in left_truncatable)) and all((isprime(i) for i in right_truncatable)):
                result.append(num)
    return sorted(result)