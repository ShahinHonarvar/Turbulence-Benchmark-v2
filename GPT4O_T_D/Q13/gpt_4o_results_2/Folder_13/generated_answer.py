def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[25:88]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]