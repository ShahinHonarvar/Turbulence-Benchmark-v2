from math import sqrt

def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[25]
    result = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s and is_prime(i):
            truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)