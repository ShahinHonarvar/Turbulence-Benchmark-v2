def find_primes_between_indices(nums):
    primes = []
    for i in range(52, 54):
        if i >= 0 and i < len(nums):
            n = nums[i]
            if n > 1:
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        break
                else:
                    primes.append(n)
    primes.sort()
    return primes