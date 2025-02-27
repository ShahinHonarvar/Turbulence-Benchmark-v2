def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    sub_list = numbers[17:79]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]