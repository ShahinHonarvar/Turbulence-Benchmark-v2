def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[1:6]
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    sorted_unique = sorted(unique_numbers, reverse=True)
    return sorted_unique[1]