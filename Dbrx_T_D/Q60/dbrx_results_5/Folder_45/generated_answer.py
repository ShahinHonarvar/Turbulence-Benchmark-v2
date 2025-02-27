from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = list(t)[61]
    result = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        num_str = str(num)
        is_l_r_truncatable = True
        for i in range(1, len(num_str) // 2 + 1):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                is_l_r_truncatable = False
                break
        if is_l_r_truncatable:
            result.append(num)
    return sorted(result)