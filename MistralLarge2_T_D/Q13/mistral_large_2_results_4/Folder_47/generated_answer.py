def find_second_largest_num(nums):
    sublist = nums[37:77]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)