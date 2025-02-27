def find_primes_between_indices(nums):
    prime_numbers = []
    for i in range(497, 931):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    break
            else:
                prime_numbers.append(nums[i])
    return sorted(prime_numbers, reverse=True)