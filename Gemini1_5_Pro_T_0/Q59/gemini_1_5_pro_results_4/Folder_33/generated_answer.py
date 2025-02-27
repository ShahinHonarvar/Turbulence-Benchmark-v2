def all_left_truncatable_prime(nums):
    x = nums[945]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 0:
            return num != 1 and num % 2 != 0
        if '0' in str(num) or num % 2 == 0:
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0:
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
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result