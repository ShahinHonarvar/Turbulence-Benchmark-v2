def find_second_smallest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 92:
        return None
    sublist = numbers[91:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]