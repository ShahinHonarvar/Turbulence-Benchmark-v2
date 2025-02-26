def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[82:87]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None