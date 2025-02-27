def find_second_smallest_num(nums):
    if len(nums) < 81:
        return None
    sublist = nums[40:81]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest