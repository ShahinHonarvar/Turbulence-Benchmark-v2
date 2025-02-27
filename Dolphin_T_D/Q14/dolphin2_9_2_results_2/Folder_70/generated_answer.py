def find_second_smallest_num(numbers):
    if 40 <= len(numbers) < 50:
        sublist = numbers[35:50]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None