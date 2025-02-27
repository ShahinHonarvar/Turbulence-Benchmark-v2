def all_left_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] and is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True