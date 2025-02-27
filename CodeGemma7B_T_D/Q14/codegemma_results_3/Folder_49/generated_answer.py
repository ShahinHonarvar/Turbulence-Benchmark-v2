def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 81 or nums[80] == nums[-1]:
        return 'None'
    return nums[81]