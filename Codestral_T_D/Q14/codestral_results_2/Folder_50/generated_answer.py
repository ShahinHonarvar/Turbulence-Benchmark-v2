def find_second_smallest_num(numbers):
    if 42 <= len(numbers) <= 68:
        sublist = sorted(numbers[42:69])
        if len(sublist) > 1:
            return sublist[1]
    return None