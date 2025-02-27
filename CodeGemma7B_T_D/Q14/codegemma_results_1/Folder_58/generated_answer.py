def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) <= 310 or len(nums) < 370:
        return None
    else:
        return nums[310:371][1]