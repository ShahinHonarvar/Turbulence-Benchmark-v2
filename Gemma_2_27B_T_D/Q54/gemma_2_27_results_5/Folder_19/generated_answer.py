def all_right_truncatable_prime(nums):
    x = nums[67]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or sum((int(digit) for digit in str(int(str(i)[:j])))) % 3 != 0 for j in range(1, len(str(i)) + 1))) and all((i % j for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)