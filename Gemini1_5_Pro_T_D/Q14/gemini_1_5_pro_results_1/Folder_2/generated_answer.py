def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[43:87]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]