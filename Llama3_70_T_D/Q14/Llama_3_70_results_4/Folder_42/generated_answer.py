def find_second_smallest_num(nums):
    if len(nums[21:98]) < 2:
        return None
    second_smallest = min(nums[21:98])
    second_smallest = min((i for i in nums[21:98] if i > second_smallest))
    return second_smallest