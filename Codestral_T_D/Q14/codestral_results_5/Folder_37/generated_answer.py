def find_second_smallest_num(numbers):
    if len(numbers) > 7:
        sublist = numbers[5:8]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None