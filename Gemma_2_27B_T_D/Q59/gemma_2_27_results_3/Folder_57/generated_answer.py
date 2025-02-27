def all_left_truncatable_prime(nums):
    x = nums[54]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x, 0, -1):
        s = str(i)
        is_left_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            primes.append(i)
    return primes