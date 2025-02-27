def all_left_truncatable_prime(nums):
    x = nums[767]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or all((int(d) % 2 and int(d) % 3 and (int(d) != 1) for d in str(int(str(i)[:j])))) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)