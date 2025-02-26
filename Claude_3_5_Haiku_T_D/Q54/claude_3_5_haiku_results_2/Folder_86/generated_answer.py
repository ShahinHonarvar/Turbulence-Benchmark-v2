def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[126]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                truncatable = False
                break
            temp //= 10
        if truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)