def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    else:
        slice_nums = nums[80:201]
        slice_nums.sort()
        if len(slice_nums) < 2:
            return None
        else:
            return slice_nums[1]