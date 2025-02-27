def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[43:87]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest