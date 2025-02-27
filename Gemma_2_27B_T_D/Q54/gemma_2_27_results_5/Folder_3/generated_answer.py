def all_right_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:-j]) for j in range(1, len(str(i))))) and is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True