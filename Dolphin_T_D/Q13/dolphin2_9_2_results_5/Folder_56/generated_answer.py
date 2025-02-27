def find_second_largest_num(nums):
    length = len(nums)
    if length > 1:
        max_num = max(nums[0], nums[1])
        second_max_num = min(nums[0], nums[1])
        for i in range(2, length):
            if nums[i] > max_num:
                second_max_num = max_num
                max_num = nums[i]
            elif nums[i] > second_max_num and nums[i] < max_num:
                second_max_num = nums[i]
        return second_max_num
    else:
        return None