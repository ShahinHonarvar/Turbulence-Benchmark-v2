def find_second_smallest_num(nums):
    try:
        nums.sort()
        return nums[91:100][1]
    except IndexError:
        return 'None'