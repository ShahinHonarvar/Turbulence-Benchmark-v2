def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = nums[0]
    second_max = None
    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max:
            second_max = num
    return second_max