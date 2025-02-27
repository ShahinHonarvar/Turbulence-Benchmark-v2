def find_second_largest_num(input_list):
    if len(input_list) < 2:
        return None
    else:
        sublist = input_list[29:94]
        largest = max(sublist)
        sublist.remove(largest)
        second_largest = max(sublist)
        return second_largest if sublist.count(second_largest) > 1 else None