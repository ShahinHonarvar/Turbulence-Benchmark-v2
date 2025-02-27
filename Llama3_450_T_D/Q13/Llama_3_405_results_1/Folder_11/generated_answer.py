def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    numbers = lst[37:52]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[-2]