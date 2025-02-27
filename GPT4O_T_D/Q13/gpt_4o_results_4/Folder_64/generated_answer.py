def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[:5]
    sublist.sort(reverse=True)
    return sublist[1]