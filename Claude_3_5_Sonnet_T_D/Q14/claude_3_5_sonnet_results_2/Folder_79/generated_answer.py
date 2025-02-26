def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    sublist = numbers[1:6]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]