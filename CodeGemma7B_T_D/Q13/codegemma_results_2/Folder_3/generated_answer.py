def find_second_largest_num(nums):
    if not nums or len(nums) < 63:
        return None
    large = float('-inf')
    second_largest = None
    for num in nums[62:93]:
        if num > large:
            second_largest = large
            large = num
        elif num > second_largest:
            second_largest = num
    return second_largest