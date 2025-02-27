def find_second_smallest_num(num_list):
    if not 310 <= len(num_list) <= 370:
        raise IndexError('List length must be between 310 and 370')
    nums = sorted(num_list[310:371])
    if len(nums) < 2:
        return 'None'
    return nums[1]