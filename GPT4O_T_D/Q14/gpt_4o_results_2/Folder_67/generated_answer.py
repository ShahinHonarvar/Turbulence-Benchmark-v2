def find_second_smallest_num(numbers):
    sub_list = numbers[50:55]
    if len(sub_list) < 2:
        return None
    unique_numbers = sorted(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]