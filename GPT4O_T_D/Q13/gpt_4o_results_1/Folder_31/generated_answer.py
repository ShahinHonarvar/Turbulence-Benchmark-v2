def find_second_largest_num(numbers):
    if len(numbers) < 89 or len(numbers[75:89]) < 2:
        return None
    sub_list = numbers[75:89]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)