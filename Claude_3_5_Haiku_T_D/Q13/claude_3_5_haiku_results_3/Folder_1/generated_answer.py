def find_second_largest_num(numbers):
    if len(numbers) < 33 or len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]