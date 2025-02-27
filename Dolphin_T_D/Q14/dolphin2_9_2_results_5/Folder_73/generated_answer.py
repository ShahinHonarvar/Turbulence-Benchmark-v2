def find_second_smallest_num(numbers):
    if 59 <= len(numbers) <= 97:
        sublist = numbers[59:98]
        sublist.sort()
        if len(sublist) >= 2:
            return sublist[1]
    return None