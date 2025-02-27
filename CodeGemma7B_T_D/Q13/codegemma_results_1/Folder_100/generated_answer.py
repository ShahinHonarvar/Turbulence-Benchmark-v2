def find_second_largest_num(nums):
    nums.sort(reverse=True)
    try:
        return nums[42:69 + 1][1]
    except IndexError:
        return 'None'