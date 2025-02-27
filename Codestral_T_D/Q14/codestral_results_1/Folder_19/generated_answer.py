def find_second_smallest_num(numbers):
    if 4 <= len(numbers) <= 8:
        sublist = sorted(numbers[4:9])
        if len(sublist) > 1:
            return sublist[1]
    return None