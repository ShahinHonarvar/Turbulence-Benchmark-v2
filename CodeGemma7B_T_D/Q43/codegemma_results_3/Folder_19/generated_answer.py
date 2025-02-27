def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[21:98]:
        if num > 1:
            is_prime = True
            for i in range(2, round(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_nums.append(num)
    return sorted(prime_nums)