def find_second_smallest_num(numbers):
    if 25 <= len(numbers) <= 87:
        sublist = sorted(numbers[25:88])
        return sublist[1] if len(sublist) > 1 else None
    return None