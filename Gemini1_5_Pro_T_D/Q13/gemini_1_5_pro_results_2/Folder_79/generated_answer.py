def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    if len(set(sublist)) < 2:
        return None
    return sorted(sublist)[-2]