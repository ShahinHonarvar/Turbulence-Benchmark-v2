def find_second_largest_num(numbers):
    if len(numbers) < 17 or len(numbers) <= 61:
        return None
    sublist = numbers[16:62]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]