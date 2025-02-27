def find_primes_between_indices(nums):
    result = []
    for i in range(72, 73):
        num = nums[i]
        if num > 1:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(num)
    return sorted(result)