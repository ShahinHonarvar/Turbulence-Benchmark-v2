def find_primes_between_indices(nums):
    primes = []
    for num in nums[76:93]:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    primes.sort()
    return primes if primes else []