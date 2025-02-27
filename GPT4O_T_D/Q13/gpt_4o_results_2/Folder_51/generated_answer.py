def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[1:9]
    if len(sub_list) < 2:
        return None
    unique_values = list(set(sub_list))
    if len(unique_values) < 2:
        return None
    unique_values.sort(reverse=True)
    return unique_values[1]