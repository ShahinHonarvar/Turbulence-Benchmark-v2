def all_left_truncatable_prime(nums):
    x = nums[803]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] and all([int(str(i)[k:]) for k in range(j + 1)]) for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes)