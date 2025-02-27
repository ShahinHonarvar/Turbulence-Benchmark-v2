def all_right_truncatable_prime(nums):
    x = nums[96]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            s = str(i)
            is_truncatable = True
            for j in range(len(s) - 1, 0, -1):
                if not int(s[:j]) in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)