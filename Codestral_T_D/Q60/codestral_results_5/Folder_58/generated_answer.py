def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    x = nums[975]
    result = []
    for n in range(x, 1, -1):
        if '0' not in str(n) and is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            result.append(n)
    result.sort(reverse=True)
    return result