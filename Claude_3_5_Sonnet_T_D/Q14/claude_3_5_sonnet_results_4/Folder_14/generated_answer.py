def find_second_smallest_num(numbers):
    if len(numbers) < 10 or len(numbers[8:10]) < 2:
        return None
    sublist = numbers[8:10]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None