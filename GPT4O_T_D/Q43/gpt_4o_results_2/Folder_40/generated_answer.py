def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    if not nums or len(nums) < 2:
        return []
    primes = []
    for num in nums[1:2]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)