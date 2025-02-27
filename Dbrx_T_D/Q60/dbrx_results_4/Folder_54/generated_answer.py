from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[88]
    result = []
    for num in range(2, x + 1):
        is_ltruncatable = all((isprime(int(str(num)[i:])) for i in range(len(str(num)))))
        if is_ltruncatable and isprime(num):
            result.append(num)
    return sorted(result, reverse=True)