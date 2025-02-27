def all_right_truncatable_prime(nums):
    x = nums[61]
    primes = []
    for i in range(2, x):
        if all((i % d for d in range(2, int(i ** 0.5) + 1))) and all((int(str(i)[:-j]) % d for d in range(2, int(int(str(i)[:-j]) ** 0.5) + 1) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)