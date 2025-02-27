def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 9:
        return None
    sublist = numbers[6:9]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort(reverse=True)
    return unique_sublist[1]