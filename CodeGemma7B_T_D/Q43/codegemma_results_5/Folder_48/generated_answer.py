def find_primes_between_indices(nums):
    results = []
    for num in nums[260:460]:
        if num <= 1:
            continue
        is_prime = True
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            results.append(num)
    return sorted(results)