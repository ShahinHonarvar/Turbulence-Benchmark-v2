def find_second_smallest_num(number_list):
    if not 30 <= len(number_list) <= 48:
        return None
    sublist = number_list[30:49]
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]