def all_left_right_truncatable_prime(nums):
    x = nums[65]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)