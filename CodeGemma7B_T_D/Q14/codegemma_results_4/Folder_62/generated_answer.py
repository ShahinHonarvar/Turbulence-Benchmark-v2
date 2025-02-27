def find_second_smallest_num(nums):
    nums.sort()
    try:
        return nums[10:67][1]
    except IndexError:
        return 'None'