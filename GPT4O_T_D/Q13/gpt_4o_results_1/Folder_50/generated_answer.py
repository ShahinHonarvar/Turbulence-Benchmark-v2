def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    sub_list = numbers[70:85]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]