def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    selected_nums = numbers[23:24]
    if len(selected_nums) < 2:
        return None
    return sorted(selected_nums)[1]