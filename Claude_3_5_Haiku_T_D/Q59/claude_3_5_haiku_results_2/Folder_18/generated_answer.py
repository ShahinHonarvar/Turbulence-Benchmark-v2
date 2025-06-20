def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[429]
    left_truncatable_primes = []
    for num in range(x):
        if '0' not in str(num):
            is_truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    is_truncatable = False
                    break
                current //= 10
            if is_truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)