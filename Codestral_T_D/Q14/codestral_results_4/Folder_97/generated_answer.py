def find_second_smallest_num(numbers):
    if 31 <= len(numbers) <= 34:
        sublist = numbers[31:35]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None