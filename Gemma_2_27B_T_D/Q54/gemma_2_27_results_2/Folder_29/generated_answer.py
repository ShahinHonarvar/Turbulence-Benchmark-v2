def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:-j]) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)