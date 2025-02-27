def all_left_truncatable_prime(nums):
    x = nums[433]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] or all((int(str(dr)[k:]) in [2, 3, 5, 7] for k in range(len(str(dr))))) for j in range(len(str(i))))) and all((int(str(i)[j:]) in [2, 3, 5, 7] for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)