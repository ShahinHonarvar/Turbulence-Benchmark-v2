def find_primes_between_indices(nums):
    primes = []
    for num in nums[25:73]:
        is_prime = True
        if num <= 1:
            is_prime = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)