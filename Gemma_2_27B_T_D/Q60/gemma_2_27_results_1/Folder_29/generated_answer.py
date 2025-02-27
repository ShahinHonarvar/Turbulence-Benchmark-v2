def all_left_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    num_str = str(num)
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return True