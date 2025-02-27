def find_second_largest_num(numbers):
    if len(numbers) <= 200 or 200 >= len(numbers):
        return None
    sublist = numbers[200:201]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    sorted_numbers = sorted(unique_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]