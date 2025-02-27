def find_second_largest_num(nums):
    if not nums:
        return None
    second_large = None
    large = None
    for num in nums[75:95]:
        if large is None or num > large:
            second_large = large
            large = num
        elif second_large is None or (num > second_large and num != large):
            second_large = num
    return second_large