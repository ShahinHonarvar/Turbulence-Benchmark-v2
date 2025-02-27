def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(1, len(nums) + 1):
        if is_prime(i):
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)

def is_prime(num):
    if num in (0, 1):
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    sq = int(num ** 0.5)
    i = 3
    while i <= sq:
        if num % i == 0:
            return False
        i += 2
    return True