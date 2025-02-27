def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    s1, s2 = (float('inf'), float('inf'))
    for num in nums:
        if num <= s1:
            s1, s2 = (num, s1)
        elif num < s2:
            s2 = num
    return s2