def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 19:
        return None
    sublist = numbers[30:49]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort(reverse=True)
    return unique_sublist[1]