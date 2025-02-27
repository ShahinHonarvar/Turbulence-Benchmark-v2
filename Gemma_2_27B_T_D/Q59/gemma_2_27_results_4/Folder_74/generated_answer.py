def all_left_truncatable_prime(nums):
    x = nums[36]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] and all((int(str(i)[k:]) % j != 0 for j in range(2, int(str(i)[k:].partition('.')[0]) ** 0.5 + 1) for k in range(len(str(i + ''))))) for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes)