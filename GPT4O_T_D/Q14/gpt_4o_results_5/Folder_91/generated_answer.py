def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[:6]
    unique_numbers = sorted(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]