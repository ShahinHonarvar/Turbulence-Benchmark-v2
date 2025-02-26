def find_second_smallest_num(numbers):
    if len(numbers) < 640 or len(numbers) < 976:
        return None
    sublist = numbers[639:976]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]