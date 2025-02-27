def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    sublist = nums[25:88]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)