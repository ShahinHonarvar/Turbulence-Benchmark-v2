def all_left_truncatable_prime(nums):
    x = nums[100]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return True
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) % 5 == 0:
                return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            res.append(i)
    res.sort(reverse=True)
    return res