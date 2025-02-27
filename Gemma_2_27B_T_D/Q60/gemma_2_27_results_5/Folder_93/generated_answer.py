def all_left_right_truncatable_prime(nums):
    x = nums[11]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s:
            is_truncatable = True
            for j in range(1, len(s)):
                if not (int(s[j:]) in primes and int(s[:-j]) in primes):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return primes