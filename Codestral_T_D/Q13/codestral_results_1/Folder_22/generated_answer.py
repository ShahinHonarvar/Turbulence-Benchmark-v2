def find_second_largest_num(numbers):
    if 40 <= len(numbers) <= 200:
        sublist = sorted(numbers[40:201], reverse=True)
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None