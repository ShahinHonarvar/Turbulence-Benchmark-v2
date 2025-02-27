def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[:9]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]