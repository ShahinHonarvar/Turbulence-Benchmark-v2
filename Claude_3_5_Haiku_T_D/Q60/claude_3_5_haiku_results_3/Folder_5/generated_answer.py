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
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = int(str(num)[1:] if len(str(num)) > 1 else num)
    return is_prime(num)

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[55]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)