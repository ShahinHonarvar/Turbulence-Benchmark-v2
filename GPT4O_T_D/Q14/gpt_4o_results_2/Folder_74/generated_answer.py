def find_second_smallest_num(numbers):
    if len(numbers) < 47 or not all((isinstance(i, (int, float)) for i in numbers[36:47])):
        return None
    sublist = numbers[36:47]
    unique_sublist = sorted(set(sublist))
    return unique_sublist[1] if len(unique_sublist) > 1 else None