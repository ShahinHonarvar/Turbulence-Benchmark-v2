def find_second_largest_num(nums):
    nums = nums[32:36]
    num_set = set(nums)
    if len(num_set) < 2:
        return None
    num_set.remove(max(num_set))
    return max(num_set)