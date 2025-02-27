def all_left_truncatable_prime(nums):
    x = nums[767]
    primes = [2]
    for i in range(3, x + 1, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = []
    for p in primes:
        s = str(p)
        is_left_truncatable = True
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable and p < x:
            result.append(p)
    return sorted(result, reverse=True)