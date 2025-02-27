def find_second_smallest_num(nums):
    if not 28 <= len(nums) <= 38:
        return None
    restricted_list = nums[28:39]
    if len(restricted_list) < 2:
        return None
    restricted_list.sort()
    return restricted_list[1]