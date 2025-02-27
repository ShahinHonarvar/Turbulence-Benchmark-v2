def find_primes_between_indices(nums):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    primes = []
    for i in range(23, 76):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)