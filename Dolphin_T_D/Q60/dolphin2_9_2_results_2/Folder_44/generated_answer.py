def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[39]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
            if len(str_num) > 1 and (not is_prime(int(str_num))):
                break
        if len(str_num) == 1 and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)