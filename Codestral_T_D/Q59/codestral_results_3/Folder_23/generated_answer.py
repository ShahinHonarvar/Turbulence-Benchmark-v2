def all_left_truncatable_prime(nums):
    x = nums[77]
    primes = [p for p in range(2, x) if all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    return sorted(primes, reverse=True)