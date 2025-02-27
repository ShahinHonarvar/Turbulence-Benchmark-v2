def find_second_largest_num(nums):
    nums = sorted(nums[27:56])[::-1]
    try:
        return nums[1]
    except IndexError:
        return 'None'