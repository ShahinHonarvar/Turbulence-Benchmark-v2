def find_second_smallest_num(nums):
    nums = sorted(nums[246:751])
    if len(nums) < 2:
        return 'None'
    else:
        return nums[1]