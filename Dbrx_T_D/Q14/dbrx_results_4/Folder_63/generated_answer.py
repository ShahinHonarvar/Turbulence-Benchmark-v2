def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    sublist = numbers[55:83]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[1]