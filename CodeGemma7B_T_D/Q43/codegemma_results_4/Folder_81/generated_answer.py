def find_primes_between_indices(nums):
    primes = []
    for num in nums[59:98]:
        if num == 2:
            primes.append(num)
        elif num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0) and (num % 11 != 0):
            primes.append(num)
    if not primes:
        return []
    return sorted(primes, reverse=True)