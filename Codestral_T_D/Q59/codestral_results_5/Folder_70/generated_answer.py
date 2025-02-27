def all_left_truncatable_prime(nums):
    x = nums[433]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))) and is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True