def all_left_right_truncatable_prime(nums):
    x = nums[30]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        n = num
        truncatable = True
        while n > 0:
            if not is_prime(n):
                truncatable = False
                break
            n //= 10
        n = num
        while n > 10:
            if not is_prime(n):
                truncatable = False
                break
            n %= 10 ** (len(str(n)) - 1)
        if truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes