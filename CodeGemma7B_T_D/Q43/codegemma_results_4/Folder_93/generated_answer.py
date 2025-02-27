def find_primes_between_indices(nums):
    primes = []
    for num in nums[70:72]:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)