def find_smallest_num(nums):
    if len(nums) < 200:
        return 'List is too short'
    elif len(nums) < 90:
        return 'List is too short to have indexes from 90 to 200'
    else:
        return min(nums[90:201])