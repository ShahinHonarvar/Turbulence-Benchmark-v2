def find_second_smallest_num(numbers):
    if len(numbers) < 200:
        return None
    sublist = numbers[30:201]
    if len(sublist) == 1:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]