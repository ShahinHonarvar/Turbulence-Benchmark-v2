def gcf_three_nums(nums):
    num1 = nums[13]
    num2 = nums[70]
    num3 = nums[32]
    gcf = float('inf')
    for i in range(3, 0, -1):
        if not (num1 % i == 0 and num2 % i == 0 and (num3 % i == 0)):
            gcf = i - 1
            break
    return gcf