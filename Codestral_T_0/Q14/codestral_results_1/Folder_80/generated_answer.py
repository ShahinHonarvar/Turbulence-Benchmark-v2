def find_second_smallest_num(numbers):
    if 30 <= len(numbers) <= 87:
        sublist = sorted(numbers[30:88])
        return sublist[1] if len(sublist) > 1 else None
    return None