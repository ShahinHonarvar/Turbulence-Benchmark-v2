def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min1, min2 = (nums[0], float('inf'))
    for num in nums[1:4]:
        if num < min1:
            min2, min1 = (min1, num)
        elif min1 < num < min2:
            min2 = num
    return min2 if min2 != float('inf') else None