def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(55, 76):
        num = nums[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums if prime_nums else []