def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 39:
        return 'None'
    else:
        subarray = nums[15:40]
        if len(subarray) > 2:
            sorted_nums = sorted(subarray)
            return sorted_nums[-2]
        else:
            return 'None'