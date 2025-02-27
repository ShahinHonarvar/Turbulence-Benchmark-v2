def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    max_num = second_max_num = nums[0]
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num