def gcf_three_nums(nums):
    if len(nums) < 35 or len(nums) < 88:
        return None
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]
    if num1 == 0 or num2 == 0 or num3 == 0:
        return 0
    else:
        gcf = min(num1, num2, num3)
        while True:
            if gcf % num1 == 0 and gcf % num2 == 0 and (gcf % num3 == 0):
                return gcf
            else:
                gcf -= 1