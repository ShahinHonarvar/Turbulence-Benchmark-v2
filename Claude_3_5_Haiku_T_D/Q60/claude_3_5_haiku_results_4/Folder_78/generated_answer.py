def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    for i in range(1, len(num_str) + 1):
        if not is_prime(int(num_str[:i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[23]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)