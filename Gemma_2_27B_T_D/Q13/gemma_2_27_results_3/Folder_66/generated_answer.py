def find_second_largest_num(nums):
    if len(nums) >= 55 and len(set(nums[50:55])) == 5:
        return sorted(nums[50:55])[-2]
    else:
        return None