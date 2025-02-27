def find_second_smallest_num(numbers):
    if 209 <= len(numbers) <= 556:
        sublist = numbers[209:557]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None