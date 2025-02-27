def find_second_smallest_num(numbers):
    if len(numbers) < 81 or len(numbers) < 41:
        return None
    sublist = numbers[40:81]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]