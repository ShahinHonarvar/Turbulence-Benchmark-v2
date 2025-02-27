def find_second_largest_num(nums):
    filtered_nums = nums[40:201]
    if len(filtered_nums) < 2:
        return None
    else:
        max_num = max(filtered_nums)
        if max_num not in filtered_nums[::-1]:
            return max_num
        else:
            return None