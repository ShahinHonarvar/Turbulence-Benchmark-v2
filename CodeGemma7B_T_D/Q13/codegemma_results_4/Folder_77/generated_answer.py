def find_second_largest_num(nums):
    nums.sort(reverse=True)
    try:
        return nums[527]
    except IndexError:
        return 'None'