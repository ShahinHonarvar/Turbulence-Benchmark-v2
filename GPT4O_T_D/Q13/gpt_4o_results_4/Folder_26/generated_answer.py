def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sublist = numbers[62:100]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1]