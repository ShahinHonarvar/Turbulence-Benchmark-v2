def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[12:64]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return sorted(prime_nums)