def find_second_smallest_num(nums):
    if not nums or len(nums) <= 35:
        return None
    nums = sorted(nums)[35:50]
    if len(nums) < 2:
        return None
    return nums[1]