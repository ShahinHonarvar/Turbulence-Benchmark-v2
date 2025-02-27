def find_second_smallest_num(numbers):
    if len(numbers) < 976 or not all((isinstance(num, (int, float)) for num in numbers)):
        return None
    sublist = numbers[639:976]
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]