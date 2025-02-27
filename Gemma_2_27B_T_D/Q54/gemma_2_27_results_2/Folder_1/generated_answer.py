def all_right_truncatable_prime(nums):
    x = nums[20]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 0, -1):
        num = i
        is_truncatable = True
        while num > 0:
            if not is_prime(num):
                is_truncatable = False
                break
            num //= 10
        if is_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)