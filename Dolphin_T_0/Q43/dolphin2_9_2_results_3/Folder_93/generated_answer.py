def find_primes_between_indices(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [nums[70]]
    if 70 != 71 or is_prime(nums[70]):
        primes.append(nums[71])
    return sorted(primes, reverse=True)