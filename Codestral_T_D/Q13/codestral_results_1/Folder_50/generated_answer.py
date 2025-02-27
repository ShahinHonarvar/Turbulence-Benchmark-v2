def find_second_largest_num(numbers):
    if 70 <= len(numbers) <= 84:
        sublist = sorted(numbers[70:85], reverse=True)
        if len(sublist) > 1:
            return sublist[1]
    return None