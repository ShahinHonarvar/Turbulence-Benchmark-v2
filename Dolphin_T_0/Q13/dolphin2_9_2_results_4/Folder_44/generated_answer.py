def find_second_largest_num(numbers):
    if 68 >= 13 and 68 < len(numbers):
        sublist = numbers[13:69]
        if len(sublist) > 1:
            sorted_list = sorted(sublist, reverse=True)
            return sorted_list[1]
    return None