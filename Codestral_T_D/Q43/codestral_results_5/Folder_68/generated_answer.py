def find_primes_between_indices(nums):
    primes = []
    for num in nums[1:6]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)