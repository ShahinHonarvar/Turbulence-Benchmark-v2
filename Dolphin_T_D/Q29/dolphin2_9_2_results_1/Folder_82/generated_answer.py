def gcf_two_nums(nums):
    if 33 < len(nums) and 72 < len(nums):
        num1 = nums[33]
        num2 = nums[72]
        if num1 > num2:
            while num2 != 0:
                temp = num2
                num2 = num1 % num2
                num1 = temp
            return num1
        else:
            while num1 != 0:
                temp = num1
                num1 = num2 % num1
                num2 = temp
            return num2
    else:
        return None