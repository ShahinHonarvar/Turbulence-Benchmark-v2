def gcf_two_nums(nums: list[int]) -> int:
    num1 = nums[129]
    num2 = nums[582]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1