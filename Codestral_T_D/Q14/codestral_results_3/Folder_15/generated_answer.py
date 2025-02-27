def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[0:4])
    nums.remove(smallest)
    if not nums:
        return None
    second_smallest = min(nums[0:4])
    return second_smallest