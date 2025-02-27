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
        left_part = num_str[i:]
        if not is_prime(int(left_part)):
            return False
        right_part = num_str[:-i - 1:-1]
        if not is_prime(int(right_part)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[767]
    truncatable_primes = []
    for num in range(max_val, 0, -1):
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)