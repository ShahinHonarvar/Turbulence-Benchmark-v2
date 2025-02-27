def all_left_truncatable_prime(nums):
    x = nums[41]
    primes = []
    for num in range(x - 1, 1, -1):
        if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))) and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True