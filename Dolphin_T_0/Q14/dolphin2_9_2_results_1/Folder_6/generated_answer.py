def find_second_smallest_num(nums):
    if not nums:
        return None
    filtered_nums = nums[29:80]
    if len(filtered_nums) < 2:
        return None
    min_num = min(filtered_nums)
    second_min = min((n for n in filtered_nums if n != min_num))
    return second_min