def find_second_largest_num(numbers):
    if len(numbers) < 21 or len(numbers) < 200:
        return None
    sublist = numbers[20:201]
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]