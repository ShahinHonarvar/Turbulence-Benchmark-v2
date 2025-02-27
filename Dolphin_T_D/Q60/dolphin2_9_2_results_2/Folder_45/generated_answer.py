def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[61]
    trunc_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            if is_prime(num):
                if is_prime(int(str_num[1:])):
                    if is_prime(int(str_num[:-1])):
                        trunc_primes.append(num)
    return sorted(trunc_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True