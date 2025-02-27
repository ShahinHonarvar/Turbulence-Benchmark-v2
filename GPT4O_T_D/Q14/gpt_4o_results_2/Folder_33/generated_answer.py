def find_second_smallest_num(numbers):
    if len(numbers) < 747:
        return None
    sub_list = numbers[262:747]
    unique_sorted_numbers = sorted(set(sub_list))
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[1]