def find_second_largest_num(lst):
    if 28 <= len(lst) <= 38:
        lst = lst[28:39]
        unique_numbers = list(set(lst))
        unique_numbers.sort()
        if len(unique_numbers) >= 2:
            return unique_numbers[1]
        else:
            return None
    else:
        return None