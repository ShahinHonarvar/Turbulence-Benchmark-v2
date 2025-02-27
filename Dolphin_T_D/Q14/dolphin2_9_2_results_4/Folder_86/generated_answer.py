def find_second_smallest_num(nums):
    if not all((isinstance(num, (int, float)) for num in nums[33:37])):
        return 'None'
    sorted_nums = sorted(nums[33:37])
    if len(sorted_nums) < 2:
        return 'None'
    else:
        return sorted_nums[1]