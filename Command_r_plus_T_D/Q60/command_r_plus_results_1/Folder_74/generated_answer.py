def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncates = [int(str_num[i:]) for i in range(len(str_num))]
    right_truncates = [int(str_num[:i]) for i in range(1, len(str_num) + 1)]
    return left_truncates + right_truncates

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    truncatable_primes = []
    for num in range(start, end + 1):
        if '0' not in str(num) and is_prime(num):
            truncates = left_right_truncate(num)
            if all((is_prime(i) for i in truncates)):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)