def all_left_right_truncatable_prime(nums):
    x = nums[7]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(num):
        while num > 9:
            num_str = str(num)
            if not is_prime(int(num_str)):
                return False
            num = int(num_str[1:])
            if not is_prime(num):
                return False
            num = int(num_str[:-1])
        return is_prime(num)
    for i in range(2, x + 1):
        if is_truncatable(i):
            primes.append(i)
    return sorted(primes)