def find_second_smallest_num(numbers):
    if 20 <= len(numbers) <= 30:
        sublist = sorted(numbers[20:31])
        if len(sublist) > 1:
            return sublist[1]
    return None