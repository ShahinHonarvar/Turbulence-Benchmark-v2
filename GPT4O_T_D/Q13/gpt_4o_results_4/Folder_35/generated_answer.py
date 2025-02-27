def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    sub_list = numbers[30:49]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]