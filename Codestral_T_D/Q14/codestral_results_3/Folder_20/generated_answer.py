def find_second_smallest_num(numbers):
    if 75 <= len(numbers) <= 94:
        sublist = sorted(numbers[75:95])
        if len(sublist) > 1:
            return sublist[1]
    return None