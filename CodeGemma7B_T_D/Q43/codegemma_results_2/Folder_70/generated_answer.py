def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(131, 816):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)