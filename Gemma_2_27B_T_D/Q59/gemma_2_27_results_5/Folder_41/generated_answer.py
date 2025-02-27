def all_left_truncatable_prime(nums):
    x = nums[46]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            if int(s[j:]) in [0, 1] or (int(s[j:]) not in [2, 3, 5, 7] and all((int(s[j:]) % k for k in range(2, int(int(s[j:]) ** 0.5) + 1)))):
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)