def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    relevant_nums = nums[:3]
    unique_nums = list(set(relevant_nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]