def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sub_list = numbers[34:56]
    unique_numbers = sorted(set(sub_list))
    return unique_numbers[1] if len(unique_numbers) > 1 else None