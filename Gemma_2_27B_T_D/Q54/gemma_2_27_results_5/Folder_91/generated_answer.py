def all_right_truncatable_prime(nums):
    x = nums[0]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            n = int(s[j:])
            if n < 2 or any((n % k == 0 for k in range(2, int(n ** 0.5) + 1))):
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)