def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for idx, num in enumerate(nums) if 157 <= idx <= 735 and is_prime(num)]
    return sorted(primes, reverse=True)