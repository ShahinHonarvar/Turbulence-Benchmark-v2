from sympy import isprime

def all_left_right_truncatable_prime(upper_bound_tuple):
    upper_bound = upper_bound_tuple[945]
    prime_list = []
    for num in range(2, upper_bound + 1):
        if not isprime(num):
            continue
        if '0' in str(num):
            continue
        num_str = str(num)
        left_truncatable = True
        right_truncatable = True
        for _ in range(len(num_str) - 1, 0, -1):
            if not isprime(int(num_str)):
                left_truncatable = False
                break
            num_str = num_str[1:]
        num_str = str(num)
        for _ in range(len(num_str) - 1, 0, -1):
            if not isprime(int(num_str)):
                right_truncatable = False
                break
            num_str = num_str[:-1]
        if left_truncatable and right_truncatable:
            prime_list.append(num)
    return sorted(prime_list, reverse=True)