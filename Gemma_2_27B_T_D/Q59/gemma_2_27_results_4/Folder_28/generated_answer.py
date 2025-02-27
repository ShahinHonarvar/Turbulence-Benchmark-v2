def all_left_truncatable_prime(nums):
    x = nums[19]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] and all_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes)

def all_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True