def find_second_smallest_num(numbers):
    sub_list = numbers[28:41]
    if len(sub_list) < 2:
        return None
    unique_sorted_numbers = sorted(set(sub_list))
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[1]