def all_left_truncatable_prime(nums):
    x = nums[22]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(x, 1, -1):
        s = str(num)
        flag = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                flag = False
                break
        if flag and '0' not in s:
            primes.append(num)
    return sorted(primes, reverse=True)