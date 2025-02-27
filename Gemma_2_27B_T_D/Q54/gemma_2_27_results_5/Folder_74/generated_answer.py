def all_right_truncatable_prime(nums):
    x = nums[36]
    primes = []
    for i in range(2, x):
        is_prime = True
        s = str(i)
        for j in range(len(s)):
            if not is_prime or int(s[:len(s) - j]) not in primes:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes)