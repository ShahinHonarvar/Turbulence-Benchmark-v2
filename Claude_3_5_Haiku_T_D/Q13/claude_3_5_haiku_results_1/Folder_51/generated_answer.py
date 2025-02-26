def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[1:9]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1]