def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    num1 = nums[85]
    num2 = nums[36]
    num3 = nums[54]
    return gcf(gcf(num1, num2), num3)