def find_second_largest_num(nums):
    if len(nums) < 2:
        return 'None'
    first = max(nums)
    nums.remove(max(nums))
    second = max(nums)
    return second