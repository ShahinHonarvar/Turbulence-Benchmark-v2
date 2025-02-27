def find_second_smallest_num(nums):
    if len(nums) < 4:
        return 'None'
    if len(nums) == 6:
        return sorted(nums[6:9])[1]
    return sorted(nums[6:], key=lambda x: abs(x))[1]