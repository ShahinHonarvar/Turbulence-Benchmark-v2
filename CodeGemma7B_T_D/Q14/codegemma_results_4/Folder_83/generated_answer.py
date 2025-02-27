def find_second_smallest_num(num_list):
    nums = num_list[90:201]
    nums.sort()
    return nums[1] if len(nums) > 1 else 'None'