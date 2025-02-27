def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    max_num = num_tuple[11]
    left_right_truncatable_primes = []
    for n in range(2, max_num + 1):
        if '0' in str(n):
            continue
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])) or not is_prime(int(str_n[i:])):
                break
        else:
            if is_prime(n):
                left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)