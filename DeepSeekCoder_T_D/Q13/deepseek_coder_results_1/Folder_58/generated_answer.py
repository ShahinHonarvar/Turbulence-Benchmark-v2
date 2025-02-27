def find_second_largest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    sublist = numbers[209:557]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]