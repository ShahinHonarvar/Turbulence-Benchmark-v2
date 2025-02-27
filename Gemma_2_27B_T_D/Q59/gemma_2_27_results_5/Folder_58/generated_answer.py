def all_left_truncatable_prime(nums):
    x = nums[975]
    primes = []
    for i in range(x, 1, -1):
        if i not in primes:
            is_prime = True
            s = str(i)
            for j in range(len(s) - 1, 0, -1):
                if int(s[:j]) not in primes:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)