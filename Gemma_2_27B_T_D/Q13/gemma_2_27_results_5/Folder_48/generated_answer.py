def find_second_largest_num(nums):
    if len(nums) >= 73 and 533 <= len(nums) and (len(nums) >= 605):
        return sorted(nums[533:606])[-2]
    return None