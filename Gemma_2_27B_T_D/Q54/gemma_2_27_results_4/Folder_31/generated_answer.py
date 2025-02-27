def all_right_truncatable_prime(nums):
    x = nums[50]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x):
        num = i
        flag = True
        while num > 0:
            if not is_prime(num):
                flag = False
                break
            num //= 10
        if flag:
            primes.append(i)
    return sorted(primes, reverse=True)