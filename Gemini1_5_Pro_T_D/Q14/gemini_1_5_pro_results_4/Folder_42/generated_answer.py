def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sublist = numbers[21:98]
    if len(set(sublist)) == 1:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]