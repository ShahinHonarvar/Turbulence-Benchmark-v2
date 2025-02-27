def find_second_smallest_num(nums):
    sub_nums = nums[12:69] if 69 <= len(nums) else nums[12:]
    if not sub_nums:
        return None
    min1 = min(sub_nums)
    sub_nums.remove(min1)
    if not sub_nums:
        return None
    return min(sub_nums)