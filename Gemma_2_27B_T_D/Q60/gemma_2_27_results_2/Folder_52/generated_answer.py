def all_left_right_truncatable_prime(nums):
    x = nums[52]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] for i in range(len(str(num))))) and all((int(str(num)[:i]) in [2, 3, 5, 7] for i in range(len(str(num)), 0, -1))):
            primes.append(num)
    return sorted(primes, reverse=True)