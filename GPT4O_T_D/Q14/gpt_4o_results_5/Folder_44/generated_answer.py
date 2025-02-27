def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sublist = numbers[91:100]
    sublist = list(set(sublist))
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]