def all_left_right_truncatable_prime(nums):
    x = nums[92]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        if not is_prime(int(num_str)) or not is_prime(int(num_str[::-1])):
            return False
        num_str = num_str[1:-1]
    return True