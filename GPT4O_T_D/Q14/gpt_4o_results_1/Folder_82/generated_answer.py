def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[20:201]
    unique_sublist = list(sorted(set(sublist)))
    if len(unique_sublist) < 2:
        return None
    return unique_sublist[1]