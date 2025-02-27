def all_left_right_truncatable_prime(nums):
    x = nums[61]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) and int(str(i)[j:]) > 1 and all((int(str(i)[:j]) % k and int(str(i)[j:]) % k for k in range(2, int(max(int(str(i)[:j]), int(str(i)[j:])) ** 0.5) + 1))) for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)