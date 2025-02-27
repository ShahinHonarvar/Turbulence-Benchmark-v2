def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    max_num = max(nums)
    second_max_num = None
    for num in nums:
        if num != max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num