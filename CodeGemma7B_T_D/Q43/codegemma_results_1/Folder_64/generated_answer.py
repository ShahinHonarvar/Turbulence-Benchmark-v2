def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(7, 10):
        current_num = nums[i]
        is_prime = True
        for j in range(2, int(current_num ** 0.5) + 1):
            if current_num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(current_num)
    return sorted(prime_nums, reverse=True)