def find_second_smallest_num(nums):
    if len(nums) < 66:
        return None
    sub_nums = nums[10:67]
    if len(sub_nums) < 2:
        return None
    else:
        min1, min2 = (float('inf'), float('inf'))
        for num in sub_nums:
            if num < min1:
                min1, min2 = (num, min1)
            elif min1 < num < min2:
                min2 = num
        if min2 == float('inf'):
            return None
        else:
            return min2