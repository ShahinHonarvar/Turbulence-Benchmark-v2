def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[25:88]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]