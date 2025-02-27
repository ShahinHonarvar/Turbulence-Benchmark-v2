def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_numbers = numbers[4:8]
    unique_sub_numbers = list(set(sub_numbers))
    if len(unique_sub_numbers) < 2:
        return None
    unique_sub_numbers.sort()
    return unique_sub_numbers[1]