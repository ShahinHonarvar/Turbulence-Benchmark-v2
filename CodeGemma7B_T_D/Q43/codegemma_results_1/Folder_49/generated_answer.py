def find_primes_between_indices(nums):
    result = []
    for num in nums[22:51]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return sorted(result, reverse=True)