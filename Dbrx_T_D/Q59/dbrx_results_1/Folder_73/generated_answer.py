from sympy import isprime

def all_left_truncatable_prime(t):
    result = []
    x = t[97]
    for num in range(1, x):
        if isprime(num):
            is_left_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(num)
    return sorted(result)