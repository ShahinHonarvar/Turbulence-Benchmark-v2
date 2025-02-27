def find_second_largest_num(numbers):
    sub_list = numbers[667:775]
    if len(sub_list) < 2:
        return None
    sorted_unique_numbers = sorted(set(sub_list), reverse=True)
    return sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None