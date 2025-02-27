def all_left_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            if int(s[j:]) not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)