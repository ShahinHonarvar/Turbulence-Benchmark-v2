def find_second_smallest_num(num_list):
    if len(num_list) < 85 or not all((isinstance(num, int) for num in num_list)):
        raise ValueError('Invalid input list.')
    nums = sorted(num_list[75:86])
    if len(nums) < 2:
        return None
    return nums[1]