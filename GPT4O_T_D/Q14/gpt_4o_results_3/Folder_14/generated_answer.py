def find_second_smallest_num(numbers):
    sub_list = numbers[8:10]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]