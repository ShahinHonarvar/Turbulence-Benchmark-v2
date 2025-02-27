def find_second_smallest_num(nums):
    if not nums or len(nums) < 209 or len(nums) > 556:
        return 'None'
    nums = sorted(nums[209:557])
    if len(nums) < 2:
        return 'None'
    return nums[1]