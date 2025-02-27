def find_second_smallest_num(numbers):
    if 5 <= len(numbers) <= 7:
        sublist = sorted(numbers[5:8])
        if len(sublist) > 1:
            return sublist[1]
    return None