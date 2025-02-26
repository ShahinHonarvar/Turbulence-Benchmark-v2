def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        current_num = int(str_n)
        if not is_prime(current_num):
            return False
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(tup):
    x = tup[57]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes