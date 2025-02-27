def find_second_smallest_num(numbers):
    sub_list = numbers[27:56]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) >= 2 else None