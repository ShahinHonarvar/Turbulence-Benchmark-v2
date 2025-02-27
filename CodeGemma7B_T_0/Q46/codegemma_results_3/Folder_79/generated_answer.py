def gcf_three_nums(nums):
    num1 = nums[16]
    num2 = nums[87]
    num3 = nums[95]
    return gcf(num1, gcf(num2, num3))