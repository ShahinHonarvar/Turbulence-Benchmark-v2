def all_left_truncatable_prime(nums):
    x = nums[24]
    primes = [True] * x
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    result = []
    for i in range(2, x):
        if primes[i]:
            s = str(i)
            is_truncatable = True
            for j in range(1, len(s)):
                if not primes[int(s[j:])]:
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    return sorted(result)