def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[100:201]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]