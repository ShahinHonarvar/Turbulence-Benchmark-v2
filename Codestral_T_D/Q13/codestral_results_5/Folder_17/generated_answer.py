def find_second_largest_num(numbers):
    if 62 <= len(numbers) <= 78:
        sublist = sorted(numbers[62:79], reverse=True)
        if len(sublist) > 1:
            return sublist[1]
    return None