def find_primes_between_indices(nums):
    primes = []
    for i in range(33, 36):
        num = nums[i]
        is_prime = True
        if num <= 1:
            is_prime = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes