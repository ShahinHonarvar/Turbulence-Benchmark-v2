def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        left_part = num_str[i:]
        right_part = num_str[:-i]
        if not (is_prime(int(left_part)) and is_prime(int(right_part))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 91:
            break
        if left_right_truncatable_prime(num) and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)