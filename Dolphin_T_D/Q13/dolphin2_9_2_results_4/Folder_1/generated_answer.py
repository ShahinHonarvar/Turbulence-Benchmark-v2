def find_second_largest_num(nums):
    if not nums:
        return None
    if len(nums) < 2:
        return None
    nums = nums[31:73]
    max_num = None
    second_max_num = None
    for num in nums:
        if max_num is None or num > max_num:
            second_max_num = max_num
            max_num = num
        elif (second_max_num is None or num > second_max_num) and num != max_num:
            second_max_num = num
    return second_max_num