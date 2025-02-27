def all_right_truncatable_prime(nums):
    x = nums[429]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 0, -1):
        i_str = str(i)
        is_truncatable = True
        for j in range(len(i_str)):
            if not is_prime(int(i_str[:j + 1])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)