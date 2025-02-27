def all_left_truncatable_prime(nums):
    x = nums[175]
    primes = []
    for num in range(2, x):
        if not any((int(str(num)[:i]) < 2 or int(str(num)[:i]) % j == 0 for i in range(1, len(str(num))) for j in range(2, int(str(num)[:i]) ** 0.5 + 1))):
            primes.append(num)
    return sorted(primes)