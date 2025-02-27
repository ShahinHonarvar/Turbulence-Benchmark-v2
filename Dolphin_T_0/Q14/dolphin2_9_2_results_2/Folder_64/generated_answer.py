def find_second_smallest_num(num_list):
    if len(num_list) < 5:
        return None
    nums = num_list[:5]
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 2:
        return None
    else:
        return nums[1]