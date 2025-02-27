def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    sublist = numbers[40:81]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]