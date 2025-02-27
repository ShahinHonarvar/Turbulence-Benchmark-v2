def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sublist = nums[:4]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None