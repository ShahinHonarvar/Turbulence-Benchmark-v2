def find_second_smallest_num(nums):
    if len(nums) == 0 or len(nums) < 200:
        return 'None'
    sublist = nums[20:201]
    if len(sublist) < 2:
        return 'None'
    sublist.sort()
    return sublist[1]