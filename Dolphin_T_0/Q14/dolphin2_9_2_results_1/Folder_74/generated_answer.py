def find_second_smallest_num(nums):
    if len(nums) < 47:
        return 'None'
    else:
        sublist = nums[36:47]
        if len(sublist) < 2:
            return 'None'
        else:
            return sorted(sublist)[1]