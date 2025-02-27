def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[29:94]
    unique_sorted_numbers = sorted(set(sub_list), reverse=True)
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[1]