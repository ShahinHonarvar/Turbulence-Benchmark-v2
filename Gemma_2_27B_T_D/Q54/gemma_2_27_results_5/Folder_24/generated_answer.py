def all_right_truncatable_prime(nums):
    x = nums[65]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            num = int(s[:len(s) - j])
            for k in range(2, int(num ** 0.5) + 1):
                if num % k == 0:
                    is_prime = False
                    break
            if not is_prime:
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)