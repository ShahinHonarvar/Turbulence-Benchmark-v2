def find_second_largest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 7:
        return None
    sublist = numbers[5:8]
    unique_sublist = list(set(sublist))
    unique_sublist.sort(reverse=True)
    if len(unique_sublist) < 2:
        return None
    return unique_sublist[1]