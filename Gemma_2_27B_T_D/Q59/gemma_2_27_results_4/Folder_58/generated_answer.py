def all_left_truncatable_prime(nums):
    x = nums[975]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)