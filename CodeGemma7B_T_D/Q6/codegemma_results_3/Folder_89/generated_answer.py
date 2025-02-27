def all_neg_ints_exclusive(input_list):
    if any((num < 0 and 51 <= input_list.index(num) < 76 for num in input_list)):
        return [num for num in input_list if num < 0 and 51 <= input_list.index(num) < 76]
    else:
        return []