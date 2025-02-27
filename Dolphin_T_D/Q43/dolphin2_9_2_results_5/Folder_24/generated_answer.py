def find_primes_between_indices(nums):

    def is_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    return sorted([nums[i] for i in range(38, 56) if is_prime(nums[i])], reverse=True)