def find_second_smallest_num(numbers):
    sub_array = numbers[8:10]
    if len(sub_array) < 2:
        return None
    unique_numbers = list(set(sub_array))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]