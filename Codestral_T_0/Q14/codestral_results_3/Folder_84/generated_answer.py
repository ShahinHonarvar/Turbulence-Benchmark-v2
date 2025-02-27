def find_second_smallest_num(numbers):
    if 40 <= len(numbers) <= 80:
        sublist = sorted(numbers[40:81])
        if len(sublist) > 1:
            return sublist[1]
    return None