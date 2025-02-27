def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set(nums[80])
    if is_prime(nums[80]):
        return set(nums[80])
    prime_factors = set()
    i = 2
    while i * i <= nums[80]:
        if nums[80] % i:
            i += 1
        else:
            nums[80] //= i
            prime_factors.add(i)
    if nums[80] > 1:
        prime_factors.add(nums[80])
    return prime_factors