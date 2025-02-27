def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 60:
        return None
    sublist = numbers[60:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]