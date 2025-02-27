def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min_1 = min(nums)
    min_2 = None
    for num in nums:
        if num != min_1 and (min_2 is None or num < min_2):
            min_2 = num
    return min_2