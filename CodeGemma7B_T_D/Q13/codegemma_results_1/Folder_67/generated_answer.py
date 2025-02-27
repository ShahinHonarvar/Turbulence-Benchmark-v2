def find_second_largest_num(nums):
    sorted_nums = sorted(nums[22:51])
    if len(sorted_nums) < 2:
        return 'None'
    return sorted_nums[-2]