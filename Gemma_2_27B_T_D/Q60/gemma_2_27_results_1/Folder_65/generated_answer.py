def all_left_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
            return False
    return True