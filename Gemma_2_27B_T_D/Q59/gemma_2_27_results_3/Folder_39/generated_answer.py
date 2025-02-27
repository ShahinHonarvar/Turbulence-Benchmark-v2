def all_left_truncatable_prime(nums):
    x = nums[30]
    primes = []
    for i in range(2, x):
        is_prime = True
        s = str(i)
        for j in range(1, len(s)):
            if int(s[j:]) not in primes:
                is_prime = False
                break
        if is_prime and all((int(d) != 0 for d in s)):
            primes.append(i)
    primes.sort(reverse=True)
    return primes