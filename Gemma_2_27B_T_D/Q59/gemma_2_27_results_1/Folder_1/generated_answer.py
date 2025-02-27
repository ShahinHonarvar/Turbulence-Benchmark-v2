def all_left_truncatable_prime(nums):
    x = nums[20]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) > 1 and all((int(str(i)[k:]) % int(str(i)[k:]) != 0 for k in range(j, len(str(i))))) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)