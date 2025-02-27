def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    largest = max(nums[32:36])
    nums[32:36].remove(largest)
    return max(nums[32:36])