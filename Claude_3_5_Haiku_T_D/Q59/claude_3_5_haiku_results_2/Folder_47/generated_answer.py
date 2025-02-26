def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[49]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            is_left_truncatable = True
            str_n = str(n)
            while len(str_n) > 1:
                str_n = str_n[1:]
                truncated_num = int(str_n)
                if not is_prime(truncated_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)