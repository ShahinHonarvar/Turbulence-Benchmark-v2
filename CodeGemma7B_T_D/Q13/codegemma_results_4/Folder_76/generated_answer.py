def find_second_largest_num(nums):
    nums.sort()
    if len(nums) <= 1:
        return 'None'
    if 686 >= len(nums) or 987 >= len(nums):
        return 'None'
    if nums[-2] == nums[-1]:
        return 'None'
    return nums[-2]