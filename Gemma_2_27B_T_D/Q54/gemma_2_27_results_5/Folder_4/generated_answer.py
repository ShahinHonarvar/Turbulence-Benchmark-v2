def all_right_truncatable_prime(nums):
    x = nums[96]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        str_i = str(i)
        right_truncatable = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[:len(str_i) - j])):
                right_truncatable = False
                break
        if right_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)