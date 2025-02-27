def find_second_smallest_num(numbers):
    if 43 <= len(numbers) <= 51:
        sublist = sorted(numbers[43:52])
        if len(sublist) > 1:
            return sublist[1]
    return None