def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    sub_array = numbers[75:95]
    if len(sub_array) < 2:
        return None
    unique_numbers = list(set(sub_array))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]