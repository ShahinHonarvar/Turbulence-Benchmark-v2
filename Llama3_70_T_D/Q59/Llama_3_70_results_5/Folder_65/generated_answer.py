def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[32]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' not in str(num) and all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)