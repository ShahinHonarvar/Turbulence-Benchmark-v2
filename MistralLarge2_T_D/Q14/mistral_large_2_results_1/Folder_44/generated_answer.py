def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    sublist = sorted(numbers[91:100])
    if len(sublist) < 2:
        return None
    return sublist[1]