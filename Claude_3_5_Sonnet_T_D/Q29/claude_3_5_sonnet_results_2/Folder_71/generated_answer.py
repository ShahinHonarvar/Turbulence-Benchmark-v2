def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 93 and isinstance(nums[78], int) and isinstance(nums[93], int) and (nums[78] > 0) and (nums[93] > 0):
        return gcd(nums[78], nums[93])
    else:
        return None