def find_second_smallest_num(numbers):
    if 262 <= len(numbers) <= 746:
        sublist = sorted(numbers[262:747])
        if len(sublist) > 1:
            return sublist[1]
    return None