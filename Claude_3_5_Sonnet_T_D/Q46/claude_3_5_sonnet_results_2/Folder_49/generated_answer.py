def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 78:
        return None
    num1, num2, num3 = (nums[34], nums[38], nums[77])
    return gcf(gcf(num1, num2), num3)