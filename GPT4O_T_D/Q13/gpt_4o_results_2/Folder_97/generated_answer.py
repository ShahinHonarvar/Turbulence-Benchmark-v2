def find_second_largest_num(numbers):
    if len(numbers) < 82:
        return None
    sublist = numbers[40:81]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]