def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 639 > 975 or 975 >= len(numbers):
        return None
    sub_list = numbers[639:976]
    if len(sub_list) < 2:
        return None
    sorted_unique_numbers = sorted(set(sub_list))
    return sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None