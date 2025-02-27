def all_odd_ints_inclusive(nums, start_index, end_index):
    return [num for num in nums[start_index:end_index + 1] if num % 2 != 0]