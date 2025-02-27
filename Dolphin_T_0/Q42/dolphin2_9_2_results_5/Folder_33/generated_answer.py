def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    num = nums[321]
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            prime_set.add(i)
    return prime_set