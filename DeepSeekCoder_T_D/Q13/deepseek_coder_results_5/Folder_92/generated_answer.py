def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[:2]
    sublist.sort(reverse=True)
    return sublist[1]