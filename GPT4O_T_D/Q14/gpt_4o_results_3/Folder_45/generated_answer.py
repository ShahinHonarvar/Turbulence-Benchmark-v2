def find_second_smallest_num(numbers):
    if len(numbers) < 31 or len(numbers) < 201:
        return None
    sublist = numbers[30:201]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]