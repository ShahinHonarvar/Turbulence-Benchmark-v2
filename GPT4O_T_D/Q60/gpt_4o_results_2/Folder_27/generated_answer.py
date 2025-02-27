def all_left_right_truncatable_prime(nums):
    if len(nums) <= 79:
        return []
    x = nums[79]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                return False
        return True
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)