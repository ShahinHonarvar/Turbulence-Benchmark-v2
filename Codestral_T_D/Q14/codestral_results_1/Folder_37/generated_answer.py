def find_second_smallest_num(numbers):
    if len(numbers) >= 8:
        sublist = numbers[5:8]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None