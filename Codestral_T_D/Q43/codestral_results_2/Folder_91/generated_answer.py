def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(nums[0], nums[1] + 1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)