def all_right_truncatable_prime(nums):
    x = nums[52]
    primes = []
    for num in range(x, 0, -1):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] or is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True