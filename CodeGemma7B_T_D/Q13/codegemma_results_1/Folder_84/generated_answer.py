def find_second_largest_num(nums):
    nums.sort(reverse=True)
    index = bisect.bisect_left(nums, nums[42])
    if index <= 42 or index > 86:
        return None
    return nums[index]