def find_second_smallest_num(numbers):
    if len(numbers) < 11 or len(numbers[10:11]) < 2:
        return None
    sublist = numbers[10:11]
    return sorted(set(sublist))[1] if len(set(sublist)) >= 2 else None