def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[15:52]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]