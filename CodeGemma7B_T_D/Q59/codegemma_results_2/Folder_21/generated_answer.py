def all_left_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num) or '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return True
    nums = sorted(set([num for num in nums if is_left_truncatable_prime(num)]))
    res = [num for num in nums if num <= nums[175]]
    return res