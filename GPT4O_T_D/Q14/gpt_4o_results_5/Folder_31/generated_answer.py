def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[29:94]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    sorted_numbers = sorted(unique_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]