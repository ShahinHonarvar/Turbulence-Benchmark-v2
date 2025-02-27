def find_second_largest_num(numbers):
    if len(numbers) < 101:
        return None
    sublist = numbers[100:201]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]