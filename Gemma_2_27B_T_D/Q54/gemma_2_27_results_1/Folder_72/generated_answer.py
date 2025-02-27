def all_right_truncatable_prime(nums):
    x = nums[31]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:-i]) for i in range(1, len(str(num)) + 1) if int(str(num)[:-i]) > 1)) and all((int(str(num)[:-i]) % j for j in range(2, int(int(str(num)[:-i]) ** 0.5) + 1) if int(str(num)[:-i]) % j)):
            primes.append(num)
    return sorted(primes, reverse=True)