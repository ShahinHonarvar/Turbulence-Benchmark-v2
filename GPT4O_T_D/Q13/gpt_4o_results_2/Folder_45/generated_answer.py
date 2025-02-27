def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sub_list = numbers[30:201]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]