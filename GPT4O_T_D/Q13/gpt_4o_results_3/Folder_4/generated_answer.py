def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = numbers[12:93]
    sorted_unique_numbers = sorted(set(sub_list))
    if len(sorted_unique_numbers) < 2:
        return None
    return sorted_unique_numbers[-2]