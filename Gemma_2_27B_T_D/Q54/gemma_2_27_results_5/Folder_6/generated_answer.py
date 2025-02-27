def all_right_truncatable_prime(nums):
    x = nums[74]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                primes.append(i)
    return sorted(primes)