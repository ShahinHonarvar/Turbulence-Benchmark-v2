def all_right_truncatable_prime(nums):
    x = nums[370]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) is prime for i in range(len(str(num)), 0, -1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True