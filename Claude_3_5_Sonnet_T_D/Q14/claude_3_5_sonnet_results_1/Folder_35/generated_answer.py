def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sublist = numbers[15:40]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = min((x for x in sublist if x != smallest))
    return second_smallest