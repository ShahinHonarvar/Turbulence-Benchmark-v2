def find_second_smallest_num(nums):
    sub_nums = nums[31:73]
    if not sub_nums:
        return None
    min_num = min(sub_nums)
    second_min_num = None
    for num in sub_nums:
        if num != min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    return second_min_num