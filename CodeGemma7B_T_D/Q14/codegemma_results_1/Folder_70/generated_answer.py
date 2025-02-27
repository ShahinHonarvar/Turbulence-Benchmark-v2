def find_second_smallest_num(nums):
    nums = sorted(nums)[35:50]
    return nums[1] if len(nums) >= 2 else None