def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    sub_list = numbers[209:557]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(sorted(sub_list))
    return unique_numbers[1]