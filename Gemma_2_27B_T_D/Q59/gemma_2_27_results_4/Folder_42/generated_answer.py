def all_left_truncatable_prime(nums):
    x = nums[64]
    primes = []
    for i in range(x, 1, -1):
        if all((int(str(i[:j])) is prime for j in range(1, len(str(i)) + 1) if str(i[:j])[0] != '0')):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True