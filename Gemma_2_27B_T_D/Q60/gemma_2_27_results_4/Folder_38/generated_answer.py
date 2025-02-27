def all_left_right_truncatable_prime(nums):
    x = nums[28]
    primes = []
    for i in range(2, x + 1):
        if i >= 10:
            s = str(i)
            is_prime = True
            for j in range(1, len(s)):
                if not (int(s[j:]) in primes and int(s[:-j]) in primes):
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        elif i in [2, 3, 5, 7]:
            primes.append(i)
    return primes