def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    sub_list = numbers[31:35]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]