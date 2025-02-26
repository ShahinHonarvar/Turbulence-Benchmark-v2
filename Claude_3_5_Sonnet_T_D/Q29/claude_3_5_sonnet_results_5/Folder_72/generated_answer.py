def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 37 and isinstance(nums[18], int) and isinstance(nums[37], int):
        return gcd(nums[18], nums[37])
    else:
        return None