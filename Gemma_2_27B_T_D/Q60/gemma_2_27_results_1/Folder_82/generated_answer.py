def all_left_right_truncatable_prime(nums):
    x = nums[69]
    primes = []
    for i in range(2, x + 1):
        if all([int(str(i)[:j]) > 1 and int(str(i)[:j]) in [2, 3, 5, 7] or all([int(str(k), 10) > 1 and str(k)[-1] != '0' for k in [str(i)[:j], str(i)[j:]]]) for j in range(1, len(str(i)))]) and all([int(str(i)[j:]) > 1 and int(str(i)[j:]) in [2, 3, 5, 7] or all([int(str(k), 10) > 1 for k in [str(i)[:i - j], str(i)[j:]]]) for j in range(1, len(str(i)))]):
            primes.append(i)
    return sorted(primes, reverse=True)