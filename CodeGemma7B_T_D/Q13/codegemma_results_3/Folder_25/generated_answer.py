def find_second_largest_num(nums: list) -> int:
    start_index = 29
    end_index = 93
    nums.sort()
    if end_index - start_index + 1 < 2:
        return None
    return nums[end_index - 1]