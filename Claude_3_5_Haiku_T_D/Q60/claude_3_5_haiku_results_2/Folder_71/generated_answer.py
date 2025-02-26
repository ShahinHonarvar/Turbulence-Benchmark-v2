def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[22]
    truncatable_primes = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        if not is_prime(n):
            continue
        is_truncatable = True
        right_trunc = n
        while right_trunc > 9:
            right_trunc //= 10
            if not is_prime(right_trunc):
                is_truncatable = False
                break
        left_trunc = n
        str_left_trunc = str(n)
        while len(str_left_trunc) > 1:
            str_left_trunc = str_left_trunc[1:]
            left_trunc_num = int(str_left_trunc)
            if not is_prime(left_trunc_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(n)
    return truncatable_primes