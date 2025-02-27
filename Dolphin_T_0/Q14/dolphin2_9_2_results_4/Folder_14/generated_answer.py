def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[8:10]
    sublist.sort()
    return sublist[1]