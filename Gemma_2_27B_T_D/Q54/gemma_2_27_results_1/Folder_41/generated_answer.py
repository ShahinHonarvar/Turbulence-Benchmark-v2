def all_right_truncatable_prime(nums):
    x = nums[46]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            s = str(i)
            right_truncatable = True
            for k in range(len(s) - 1, 0, -1):
                if int(s[:k]) not in primes:
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)