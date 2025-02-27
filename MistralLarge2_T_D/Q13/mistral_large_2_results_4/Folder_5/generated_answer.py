def find_second_largest_num(numbers):
    if len(numbers) >= 10:
        sublist = numbers[8:10]
        if len(sublist) == 2:
            return sorted(sublist)[-2]
    return None