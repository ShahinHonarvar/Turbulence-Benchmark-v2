def all_left_truncatable_prime(nums):
    x = nums[760]
    primes = []
    for possiblePrime in range(x, 1, -1):
        if all((int(str(possiblePrime)[i:]) in primes or is_prime(int(str(possiblePrime)[i:])) for i in range(len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True