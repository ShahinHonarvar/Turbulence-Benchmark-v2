def find_second_smallest_num(nums):
    nums.sort()
    try:
        return nums[29:52][1]
    except IndexError:
        return 'None'