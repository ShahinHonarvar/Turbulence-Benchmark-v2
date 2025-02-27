def all_right_truncatable_prime(nums):
    x = nums[35]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        num_str = str(i)
        is_rt_prime = True
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                is_rt_prime = False
                break
            num_str = num_str[:-1]
        if is_rt_prime:
            primes.append(i)
    return sorted(primes, reverse=True)