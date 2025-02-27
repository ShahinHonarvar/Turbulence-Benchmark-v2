def find_second_smallest_num(num_list):
    nums = num_list[80:201]
    nums.sort()
    if len(nums) == 0:
        return 'None'
    return nums[1]