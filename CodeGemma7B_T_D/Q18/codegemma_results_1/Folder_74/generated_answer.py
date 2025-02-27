def sum_ints_div_by_either_nums(nums):
    if 90 <= len(nums) and len(nums) <= 97:
        sum = 0
        for index in range(90, 98):
            if nums[index] % 13 == 0 and nums[index] % 35 != 0 or (nums[index] % 13 != 0 and nums[index] % 35 == 0):
                sum += nums[index]
        return sum
    else:
        return 0