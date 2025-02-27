def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[87:89 + 1]:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return sorted(prime_nums) if prime_nums else []