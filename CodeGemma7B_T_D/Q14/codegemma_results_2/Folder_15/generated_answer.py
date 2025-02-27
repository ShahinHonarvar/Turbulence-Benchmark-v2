def find_second_smallest_num(nums):
    nums.sort()
    try:
        return nums[1:4]
    except IndexError:
        return 'None'