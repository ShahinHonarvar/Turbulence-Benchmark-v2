def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    sublist = nums[30:88]
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]