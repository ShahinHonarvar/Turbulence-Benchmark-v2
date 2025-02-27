def find_second_smallest_num(lst):
    nums = lst[:9]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]