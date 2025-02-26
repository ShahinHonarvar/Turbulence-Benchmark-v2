def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 375:
        return None
    num1, num2, num3 = (nums[341], nums[238], nums[374])
    return gcf(gcf(num1, num2), num3)