def all_right_truncatable_prime(nums):
    x = nums[370]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x - 1, 1, -1):
        s = str(i)
        is_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[:len(s) - j])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)