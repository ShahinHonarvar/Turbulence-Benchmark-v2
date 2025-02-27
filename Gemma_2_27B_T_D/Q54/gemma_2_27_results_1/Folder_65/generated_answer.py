def all_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:-j]) > 1 and IsPrime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)

def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True