def all_left_right_truncatable_prime(nums):
    x = nums[77]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:]) in [2, 3, 5, 7] for j in range(len(str(i))))) and all((int(str(i)[:j]) in [2, 3, 5, 7] for j in range(1, len(str(i)) + 1))) and all((int(str(i)[j:]) in [2, 3, 5, 7] for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return primes