def all_left_truncatable_prime(nums):
    x = nums[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        s = str(i)
        flag = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                flag = False
                break
        if flag and '0' not in s:
            primes.append(i)
    return sorted(primes, reverse=True)