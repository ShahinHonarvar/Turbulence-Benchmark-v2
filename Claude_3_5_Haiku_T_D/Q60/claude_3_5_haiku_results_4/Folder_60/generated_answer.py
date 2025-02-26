def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        left = int(str_num[i:])
        right = int(str_num[:-i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[87]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)