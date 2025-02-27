def find_second_largest_num(numbers):
    if len(numbers) < 976:
        return None
    sub_range = numbers[639:976]
    unique_numbers = list(set(sub_range))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]