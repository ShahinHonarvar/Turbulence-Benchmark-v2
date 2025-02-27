def all_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for i in range(2, x):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            if not is_prime:
                break
            n = int(s[j:])
            if n < 2 or any((n % j == 0 for j in range(2, int(n ** 0.5) + 1))):
                is_prime = False
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)