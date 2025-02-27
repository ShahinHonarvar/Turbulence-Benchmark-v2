def find_second_smallest_num(numbers):
    if 20 <= len(numbers) <= 200:
        sublist = sorted(numbers[20:201])
        if len(sublist) > 1:
            return sublist[1]
    return None