def find_second_largest_num(nums):
    nums = nums[29:52]
    if len(nums) == 0 or len(nums) == 1:
        return None
    largest = nums[0]
    second_largest = None
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest