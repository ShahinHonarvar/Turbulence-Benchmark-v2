def all_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] or int(str(num)[:i]) in primes for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted([p for p in primes if all((int(str(p)[i:]) in [2, 3, 5, 7] or int(str(p)[i:]) in primes for i in range(len(str(p)))))])