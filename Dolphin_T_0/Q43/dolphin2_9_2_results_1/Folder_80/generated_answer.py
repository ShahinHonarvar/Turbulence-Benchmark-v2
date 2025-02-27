def find_primes_between_indices(nums):
    primes = []
    for num in nums[12:30]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    if primes:
        primes.sort(reverse=True)
    return primes