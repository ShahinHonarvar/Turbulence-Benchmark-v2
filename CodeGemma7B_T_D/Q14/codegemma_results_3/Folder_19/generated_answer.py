def find_second_smallest_num(nums):
    if len(nums) < 9 or not nums[4:9]:
        return None
    nums[4:9].sort()
    return nums[5]