def all_left_right_truncatable_prime(nums):
    x = nums[38]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] and int(str(i)[:j]) in [2, 3, 5, 7] for j in range(1, len(str(i))))):
            if all((j in [2, 3, 5, 7] for j in [int(str(i)[:k]) for k in reversed(range(1, len(str(i))))])):
                primes.append(i)
    return sorted(primes, reverse=True)