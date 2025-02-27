def find_second_smallest_num(nums):
    sub_nums = nums[25:52]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    second_smallest = sub_nums[1]
    for num in sub_nums:
        if num < second_smallest and num != sub_nums[0]:
            second_smallest = num
    return second_smallest