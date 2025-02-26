def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[88]
    right_truncatable_primes = []
    for num in range(2, x):
        current = num
        is_rt_prime = True
        while current > 0:
            if not is_prime(current):
                is_rt_prime = False
                break
            current //= 10
        if is_rt_prime and current == 0:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)