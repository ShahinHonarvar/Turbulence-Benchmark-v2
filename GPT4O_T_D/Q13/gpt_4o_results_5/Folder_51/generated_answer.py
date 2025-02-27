def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sub_list = numbers[1:9]
    if len(sub_list) < 2:
        return None
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)