def find_second_largest_num(lst):
    sublist = lst[527:539]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    second_max_num = None
    for num in sublist:
        if num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num