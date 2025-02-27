def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = nums[38]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            num //= i
        else:
            i += 1
    if num > 1:
        factors.add(num)
    return factors