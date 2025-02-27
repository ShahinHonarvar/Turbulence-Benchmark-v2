def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[70:201]
    if len(sublist) == 1:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]