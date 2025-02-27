def find_second_smallest_num(numbers):
    sub_list = numbers[43:52]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]