def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sub_list = numbers[20:201]
    if len(sub_list) < 2:
        return None
    unique_numbers = list(set(sub_list))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None