def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    selected_nums = numbers[13:69]
    sorted_selected_nums = sorted(selected_nums)
    if len(sorted_selected_nums) < 2:
        return None
    return sorted_selected_nums[1]