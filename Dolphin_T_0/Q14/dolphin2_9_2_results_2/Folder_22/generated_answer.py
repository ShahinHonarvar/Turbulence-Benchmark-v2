def find_second_smallest_num(lst):
    sublist = lst[200:40]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    else:
        unique_numbers.sort()
        return unique_numbers[1]