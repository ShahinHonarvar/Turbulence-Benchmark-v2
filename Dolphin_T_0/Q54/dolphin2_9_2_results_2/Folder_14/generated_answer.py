def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    while num != 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(nums):
    max_num = nums[78]
    primes = []
    for num in range(max_num, 1, -1):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)