def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:9]
    unique_sublist = list(set(sub_list))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort(reverse=True)
    return unique_sublist[1]