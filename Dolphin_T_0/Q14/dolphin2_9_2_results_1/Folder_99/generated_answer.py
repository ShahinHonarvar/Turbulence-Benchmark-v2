def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min1, min2 = (None, None)
    for num in nums:
        if min1 is None or num < min1:
            min1, min2 = (num, min1)
        elif min2 is None or num < min2:
            min2 = num
    return min2