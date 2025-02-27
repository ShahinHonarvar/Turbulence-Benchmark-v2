def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[8:10]
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if unique_numbers.index(unique_numbers[0]) == 1 else unique_numbers[1]