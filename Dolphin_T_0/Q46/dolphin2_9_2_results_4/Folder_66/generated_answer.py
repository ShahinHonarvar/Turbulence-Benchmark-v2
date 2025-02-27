def gcf_three_nums(nums):
    num1 = nums[92]
    num2 = nums[69]
    num3 = nums[95]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)