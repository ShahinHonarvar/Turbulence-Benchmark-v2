def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for idx, num in enumerate(nums) if is_prime(num) and 13 <= idx <= 29]
    return sorted(primes, reverse=True)