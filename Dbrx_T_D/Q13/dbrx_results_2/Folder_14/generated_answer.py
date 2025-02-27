def find_second_largest_num(numbers):
    sub_list = numbers[5:8]
    unique_sublist = list(set(sub_list))
    unique_sublist.sort(reverse=True)
    if len(unique_sublist) < 2:
        return None
    else:
        return unique_sublist[1]