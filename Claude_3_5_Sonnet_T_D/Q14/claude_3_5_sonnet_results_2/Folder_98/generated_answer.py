def find_second_smallest_num(numbers):
    if len(numbers) < 7 or len(numbers[6:7]) < 2:
        return None
    sublist = numbers[6:7]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1] if len(set(sublist)) >= 2 else None