def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    subarr = nums[62:100]
    if len(subarr) < 2:
        return None
    min1, min2 = (min(subarr), min(subarr))
    for num in subarr:
        if num != min1 and num < min2:
            min2 = num
    return min2 if min1 != min2 else None