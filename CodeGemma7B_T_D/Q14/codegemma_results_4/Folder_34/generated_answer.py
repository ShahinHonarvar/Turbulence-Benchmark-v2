def find_second_smallest_num(nums):
    nums.sort()
    return nums[60:201][1] if len(nums[60:201]) >= 2 else None