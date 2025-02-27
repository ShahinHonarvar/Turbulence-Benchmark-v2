def find_primes_between_indices(nums):
    primes = []
    for i in range(69, 81):
        num = nums[i]
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes