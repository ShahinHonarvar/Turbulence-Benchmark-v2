def all_left_truncatable_prime(nums):
    x = nums[177]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))) and is_prime(num):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True