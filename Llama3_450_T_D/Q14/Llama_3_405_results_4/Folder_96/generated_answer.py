def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    selected_nums = numbers[50:201]
    if len(selected_nums) < 2:
        return None
    return sorted(selected_nums)[1]