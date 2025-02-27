def find_second_smallest_num(nums):
    if len(nums) < 2:
        return 'None'
    min_num = min(nums[0:10])
    nums.remove(min_num)
    if not nums:
        return 'None'
    return min(nums[0:10])