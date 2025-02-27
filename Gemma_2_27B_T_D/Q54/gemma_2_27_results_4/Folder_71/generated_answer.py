def all_right_truncatable_prime(nums):
    x = nums[22]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(x - 1, 1, -1):
        num_str = str(num)
        is_right_truncatable = True
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                is_right_truncatable = False
                break
            num_str = num_str[:-1]
        if is_right_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)