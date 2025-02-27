def find_second_largest_num(nums):
    if len(nums) >= 56 and 13 <= len(nums) - 1 and (len(nums) - 1 <= 68):
        sorted_nums = sorted(nums[13:69], reverse=True)
        if len(sorted_nums) >= 2:
            return sorted_nums[1]
    return None