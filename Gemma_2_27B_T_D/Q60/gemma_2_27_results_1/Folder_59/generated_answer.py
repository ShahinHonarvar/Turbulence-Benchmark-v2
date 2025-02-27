def all_left_right_truncatable_prime(nums):
    x = nums[84]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s:
            is_prime = True
            for j in range(1, len(s)):
                if not int(s[j:]) or not int(s[:-j]):
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)