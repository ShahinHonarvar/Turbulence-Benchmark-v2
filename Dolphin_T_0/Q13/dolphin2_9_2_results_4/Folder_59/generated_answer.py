def find_second_largest_num(nums):
    if not 0 <= len(nums) <= 10 or len(set(nums)) != len(nums):
        return None
    first, second = (None, None)
    for num in nums:
        if num > first:
            first, second = (num, first)
        elif second < num < first:
            second = num
    return second