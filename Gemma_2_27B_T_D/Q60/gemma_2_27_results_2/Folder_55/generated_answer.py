def all_left_right_truncatable_prime(nums):
    x = nums[73]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:]) > 1 and all((int(str(i)[:k]) > 1 for k in range(1, len(str(i))))) and all((int(str(i)[j:]) in [2, 3, 5, 7] or all((int(str(i)[j:]) % d for d in range(2, int(int(str(i)[j:]) ** 0.5) + 1))) for j in range(len(str(i))))) for d in range(2, int(int(str(i)[:k]) ** 0.5) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True)