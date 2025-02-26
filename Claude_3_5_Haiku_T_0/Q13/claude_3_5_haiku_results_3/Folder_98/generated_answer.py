def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[:7]
    if len(set(sublist)) < 2:
        return None
    sorted_unique = sorted(set(sublist), reverse=True)
    return sorted_unique[1]