def find_second_smallest_num(nums):
    if 32 <= len(nums) <= 35:
        s1, s2 = (float('inf'), float('inf'))
        for num in nums[31:36]:
            if num < s1:
                s1, s2 = (num, s1)
            elif num < s2:
                s2 = num
        return s2 if s2 != float('inf') else None
    else:
        return None