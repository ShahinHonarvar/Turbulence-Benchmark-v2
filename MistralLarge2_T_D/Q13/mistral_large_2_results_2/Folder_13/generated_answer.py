def find_second_largest_num(nums):
    if len(nums) <= 87:
        sublist = nums[25:88]
        if len(sublist) < 2:
            return None
        first_max = max(sublist)
        sublist.remove(first_max)
        second_max = max(sublist)
        return second_max
    return None