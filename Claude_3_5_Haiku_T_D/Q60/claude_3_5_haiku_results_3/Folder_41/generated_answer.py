def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    truncated_str = str(num)
    while len(truncated_str) > 0:
        current_num = int(truncated_str)
        if not is_prime(current_num):
            return False
        truncated_str = truncated_str[1:]
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[46]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes