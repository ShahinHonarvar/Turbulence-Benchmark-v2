def all_right_truncatable_prime(nums):
    x = nums[84]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    right_truncatable = []
    for p in primes:
        right_truncatable_p = True
        p_str = str(p)
        while len(p_str) > 0:
            if int(p_str) not in primes:
                right_truncatable_p = False
                break
            p_str = p_str[:-1]
        if right_truncatable_p:
            right_truncatable.append(p)
    return sorted(right_truncatable, reverse=True)