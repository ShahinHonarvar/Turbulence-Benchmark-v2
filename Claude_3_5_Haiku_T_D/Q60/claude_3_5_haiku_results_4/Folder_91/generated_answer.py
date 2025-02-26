def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        right_trunc = num
        while right_trunc > 0:
            if not is_prime(right_trunc):
                is_truncatable = False
                break
            right_trunc //= 10
        left_trunc = num
        str_left_trunc = str(left_trunc)
        while len(str_left_trunc) > 1:
            str_left_trunc = str_left_trunc[1:]
            if not is_prime(int(str_left_trunc)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes