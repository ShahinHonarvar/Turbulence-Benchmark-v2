def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[:5]
    sublist.sort()
    return sublist[1]