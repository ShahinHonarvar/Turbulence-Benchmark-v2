def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncate = str_num
    right_truncate = str_num
    for i in range(len(str_num)):
        left_truncate = left_truncate[1:]
        right_truncate = right_truncate[:-1]
        if not is_prime(int(left_truncate)) or not is_prime(int(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    start, end = nums
    truncatable_primes = []
    for num in range(start, end + 1):
        if num % 10 == 0 or not is_prime(num):
            continue
        if left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)