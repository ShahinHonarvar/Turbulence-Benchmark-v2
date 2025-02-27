def all_left_truncatable_prime(nums):
    x = nums[84]
    primes = [p for p in range(2, x) if all((all((int(d) != 0 for d in str(n))) and is_prime(n) for n in [int(str(p)[i:]) for i in range(len(str(p)))]))]
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True