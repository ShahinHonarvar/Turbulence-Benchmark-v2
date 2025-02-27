def find_second_smallest_num(nums):
    if not nums[1:101]:
        return None
    min_num = min(nums[1:101])
    nums = [x for x in nums[1:101] if x != min_num]
    if not nums:
        return None
    return min(nums)