def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    first_max = max(nums[0], nums[1], nums[2])
    second_max = None
    for num in nums[:3]:
        if num != first_max:
            if second_max is None or second_max < num:
                second_max = num
    return second_max