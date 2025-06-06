def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[0:8]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]