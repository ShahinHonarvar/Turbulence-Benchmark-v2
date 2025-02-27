def find_second_largest_num(numbers):
    if len(numbers) < 747:
        return None
    sliced_list = numbers[262:747]
    unique_numbers = list(set(sliced_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]