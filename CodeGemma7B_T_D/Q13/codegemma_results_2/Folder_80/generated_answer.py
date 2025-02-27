def find_second_largest_num(nums):
    if len(nums) < 65 or max(nums) < 9:
        return 'None'
    nums64 = sorted(nums[64:67], reverse=True)
    return nums64[1] if len(nums64) > 1 else 'None'