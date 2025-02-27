def all_left_truncatable_prime(nums):
    x = nums[43]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) > 1 and all((int(str(num)[:i])[j] != 0 for j in range(i))) and all((j == 2 or int(str(num)[:i]) % j for j in range(2, int(str(num)[:i]) ** 0.5 + 1))) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes)