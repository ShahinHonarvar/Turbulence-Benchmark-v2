def all_left_right_truncatable_prime(nums):
    x = nums[38]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) > 1 and all((k > 1 and int(str(i)[:j]) % k for k in range(2, int(int(str(i)[:j]) ** 0.5) + 1))) for j in range(1, len(str(i)) + 1))) and all((int(str(i)[l:]) > 1 and all((k > 1 and int(str(i)[l:]) % k for k in range(2, int(int(str(i)[l:]) ** 0.5) + 1))) for l in range(len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)