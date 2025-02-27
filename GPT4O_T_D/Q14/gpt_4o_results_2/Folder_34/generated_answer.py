def find_second_smallest_num(numbers):
    sub_list = numbers[60:201]
    if len(sub_list) < 2:
        return None
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]