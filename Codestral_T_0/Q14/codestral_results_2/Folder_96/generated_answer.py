def find_second_smallest_num(numbers):
    if 50 <= len(numbers) <= 200:
        sublist = sorted(numbers[50:201])
        if len(sublist) > 1:
            return sublist[1]
    return None