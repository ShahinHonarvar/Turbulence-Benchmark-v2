def find_second_smallest_num(list_numbers):
    if len(list_numbers) < 200:
        return None
    sublist = sorted(list_numbers[19:200], unique=True)
    if len(sublist) < 2:
        return None
    return sublist[1]