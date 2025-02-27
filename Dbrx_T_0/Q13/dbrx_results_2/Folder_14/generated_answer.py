def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[5:8]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort(reverse=True)
    return unique_sublist[1]