def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sublist = numbers[8:10]
    if len(set(sublist)) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[0]