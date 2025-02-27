def find_second_largest_num(nums):
    if len(nums) >= 200:
        sublist = nums[200:201]
        if len(sublist) > 1:
            max_num = max(sublist)
            sublist.remove(max_num)
            second_max_num = max(sublist)
            return second_max_num
    return None