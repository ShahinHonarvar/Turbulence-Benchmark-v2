def find_second_largest_num(nums):
    try:
        selected_nums = nums[66:94]
        max_num = max(selected_nums)
        second_max_num = max([num for num in selected_nums if num != max_num])
        return second_max_num
    except (IndexError, ValueError):
        return None