def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [num for num in nums[7:10] if is_prime(num)]
    primes.sort(reverse=True)
    return primes