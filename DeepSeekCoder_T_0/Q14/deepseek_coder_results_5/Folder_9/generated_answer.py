def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 70:
        return None
    sublist = numbers[70:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]