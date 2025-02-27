def find_second_largest_num(num_list):
    nums = num_list[75:89]
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else 'None'