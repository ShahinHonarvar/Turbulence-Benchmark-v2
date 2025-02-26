def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers[29:52]) < 2:
        return None
    sublist = numbers[29:52]
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]