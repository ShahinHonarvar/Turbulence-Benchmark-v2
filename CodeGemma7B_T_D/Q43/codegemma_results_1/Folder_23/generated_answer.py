def find_primes_between_indices(nums):
    """
            This function finds the sorted list of prime numbers from index 20 to 48 (inclusive) in a given list of integers.
            """
    primes = []
    for i in range(20, 49):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    return sorted(primes, reverse=True)