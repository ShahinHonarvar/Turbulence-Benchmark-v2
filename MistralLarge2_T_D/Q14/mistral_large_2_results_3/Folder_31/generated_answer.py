def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[29:94]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest