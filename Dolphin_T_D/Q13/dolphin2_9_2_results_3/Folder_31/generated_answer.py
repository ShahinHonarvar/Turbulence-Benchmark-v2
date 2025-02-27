def find_second_largest_num(numbers):
    sublist = numbers[75:89]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    else:
        unique_numbers.sort()
        return unique_numbers[-2]