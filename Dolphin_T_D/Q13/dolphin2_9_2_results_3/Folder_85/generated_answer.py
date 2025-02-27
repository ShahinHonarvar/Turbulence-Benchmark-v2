def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    from_index = max(5, 0)
    to_index = min(8, len(nums) - 1)
    if from_index > to_index:
        return None
    subnums = nums[from_index:to_index + 1]
    unique_nums = list(set(subnums))
    if len(unique_nums) < 2:
        return None
    first_max = max(unique_nums)
    unique_nums.remove(first_max)
    second_max = max(unique_nums)
    return second_max