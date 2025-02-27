def gcf_three_nums(nums):
    num1 = nums[944]
    num2 = nums[814]
    num3 = nums[865]
    for i in range(min(num1, num2, num3), 1, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i