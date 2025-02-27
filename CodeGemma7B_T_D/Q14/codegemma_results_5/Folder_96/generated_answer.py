def find_second_smallest_num(nums):
    filtered_nums = sorted([num for num in nums[50:201] if num != min(nums)])
    return filtered_nums[1] if filtered_nums else 'None'