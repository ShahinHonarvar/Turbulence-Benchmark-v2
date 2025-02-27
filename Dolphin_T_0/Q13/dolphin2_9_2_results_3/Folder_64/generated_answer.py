def find_second_largest_num(nums):
    if not isinstance(nums, list):
        return None
    if len(nums) < 2:
        return None
    max_num = nums[0]
    second_max_num = None
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num