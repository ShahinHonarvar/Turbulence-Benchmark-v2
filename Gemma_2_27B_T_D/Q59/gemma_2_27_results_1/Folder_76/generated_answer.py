def all_left_truncatable_prime(nums):
    x = nums[370]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        s = str(i)
        is_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_truncatable = False
                break
        if is_truncatable and '0' not in s:
            primes.append(i)
    return sorted(primes, reverse=True)