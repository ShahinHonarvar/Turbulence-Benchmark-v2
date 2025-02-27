def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    else:
        min_num = min(nums[0], nums[1])
        second_min_num = max(nums[0], nums[1])
        for num in nums[2:]:
            if num < min_num:
                second_min_num = min_num
                min_num = num
            elif num < second_min_num and num != min_num:
                second_min_num = num
        return second_min_num if second_min_num != min_num else None