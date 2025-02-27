def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[43:77]:
        if is_prime(num):
            prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums if prime_nums else []