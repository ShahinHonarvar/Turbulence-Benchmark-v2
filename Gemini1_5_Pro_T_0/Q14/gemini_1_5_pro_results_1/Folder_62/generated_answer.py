def find_second_smallest_num(numbers):
    if len(numbers) < 67 or 10 > len(numbers):
        return None
    sublist = numbers[10:67]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]