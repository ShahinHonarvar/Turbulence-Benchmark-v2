def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 8 >= len(numbers):
        return None
    sublist = numbers[1:9]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None