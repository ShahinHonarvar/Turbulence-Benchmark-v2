def find_second_smallest_num(nums):
    if len(nums) < 36:
        return None
    sublist = nums[32:36]
    if len(sublist) < 2:
        return None
    try:
        smallest = min(sublist)
        sublist.remove(smallest)
        return min(sublist)
    except ValueError:
        return None