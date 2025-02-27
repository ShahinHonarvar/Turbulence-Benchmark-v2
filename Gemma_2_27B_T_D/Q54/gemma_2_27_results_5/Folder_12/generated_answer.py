def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in prime_numbers for j in range(1, len(str(i)) + 1))) and is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True