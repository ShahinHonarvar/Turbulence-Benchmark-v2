def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        left_part = num_str[:i] if i != 0 else ''
        right_part = num_str[i + 1:] if i != len(num_str) - 1 else ''
        if not is_prime(int(left_part + right_part)) or '0' in left_part + right_part:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)