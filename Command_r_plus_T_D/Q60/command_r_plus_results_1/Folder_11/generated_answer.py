def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    num_str = str(num)
    left_truncate = num_str
    right_truncate = num_str
    for _ in range(len(num_str) - 1):
        left_truncate = left_truncate[1:]
        if not is_prime(int(left_truncate)):
            break
    for _ in range(len(num_str) - 1):
        right_truncate = right_truncate[:-1]
        if not is_prime(int(right_truncate)):
            break
    return (left_truncate, right_truncate)

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num < 10:
            continue
        left_trunc, right_trunc = left_right_truncate(num)
        if left_trunc == str(num) and right_trunc == str(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)