def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 20 or len(nums) > 200:
        return 'None'
    return nums[20:201][1]