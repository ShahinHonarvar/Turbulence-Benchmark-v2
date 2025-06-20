def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = numbers[19:93]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]