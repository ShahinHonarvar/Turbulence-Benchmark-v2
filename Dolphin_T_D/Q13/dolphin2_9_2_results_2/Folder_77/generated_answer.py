def find_second_largest_num(input_list: list):
    sublist = input_list[527:539]
    if len(sublist) < 2:
        return None
    max_num = sublist[0]
    second_max = None
    for num in sublist[1:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif second_max == None or num > second_max:
            second_max = num
    return second_max