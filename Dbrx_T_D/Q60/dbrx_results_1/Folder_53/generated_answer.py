from sympy import isprime

def all_left_right_truncatable_prime(upper_bound_tuple):
    upper_bound = upper_bound_tuple[86]
    result = []
    for num in range(10, upper_bound + 1):
        if isprime(num) and (not '0' in str(num)):
            is_truncatable = True
            while num > 10:
                num = int(str(num)[1:]) if num % 10 != 0 else int(str(num)[:-1])
                if not isprime(num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)