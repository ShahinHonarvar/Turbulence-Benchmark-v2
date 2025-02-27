def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(len(nums)):
        if nums[i] <= min_num and nums[i] != min_num:
            second_min_num = min_num
            min_num = nums[i]
        elif nums[i] <= second_min_num and nums[i] != min_num and (nums[i] != second_min_num):
            second_min_num = nums[i]
    return second_min_num if second_min_num != float('inf') else None