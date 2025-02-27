def find_second_smallest_num(numbers):
    if 8 < len(numbers) <= 9 and len(set(numbers[8:9 + 1])) > 1:
        sublist = sorted(numbers[8:9 + 1])
        return sublist[1]
    else:
        return None