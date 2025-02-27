def find_second_largest_num(nums):
    if not nums or len(nums) < 2:
        return None
    max_num = nums[0]
    second_max = None
    for num in nums[1:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num < max_num:
            if second_max is None or second_max < num:
                second_max = num
    return second_max