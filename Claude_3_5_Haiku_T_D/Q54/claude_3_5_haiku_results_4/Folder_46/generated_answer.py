def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[33]
    right_truncatable_primes = []
    for num in range(2, x):
        temp = num
        is_truncatable = True
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)