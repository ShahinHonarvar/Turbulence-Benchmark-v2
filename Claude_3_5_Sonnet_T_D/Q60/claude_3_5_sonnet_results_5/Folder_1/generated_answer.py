def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            left = int(s[i:])
            right = int(s[:-i])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    x = nums[20]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)