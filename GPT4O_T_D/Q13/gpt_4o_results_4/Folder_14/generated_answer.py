def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[5:8]
    if len(sub_list) < 2:
        return None
    sorted_unique_numbers = sorted(set(sub_list), reverse=True)
    if len(sorted_unique_numbers) < 2:
        return None
    return sorted_unique_numbers[1]