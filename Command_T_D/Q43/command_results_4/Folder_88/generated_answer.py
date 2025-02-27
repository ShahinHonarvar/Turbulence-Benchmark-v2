def find_primes_between_indices(nums):
    result = []
    for i in range(66, 81 + 1):
        is_prime = all((nums[j] != i for j in range(i ** 2, int(i ** 2 + i) + 1, i + 1)))
        if is_prime:
            result.append(i)
    return result