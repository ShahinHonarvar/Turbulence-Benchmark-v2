def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    sublist = nums[30:49]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist)
    return second_largest