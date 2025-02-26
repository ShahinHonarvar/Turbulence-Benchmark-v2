def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[61]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        right_trunc = num
        while right_trunc > 0:
            if not is_prime(right_trunc):
                is_left_right_truncatable = False
                break
            right_trunc //= 10
        if is_left_right_truncatable:
            left_trunc_str = str(num)
            while len(left_trunc_str) > 0:
                if not is_prime(int(left_trunc_str)):
                    is_left_right_truncatable = False
                    break
                left_trunc_str = left_trunc_str[1:]
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)