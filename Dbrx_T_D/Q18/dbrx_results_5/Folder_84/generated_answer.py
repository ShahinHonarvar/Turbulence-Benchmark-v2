def sum_ints_div_by_either_nums(numbers):
    sub_list = numbers[78:82]
    return sum((x for x in sub_list if x % 76 == 0 or x % 60 == 0)) if len(sub_list) >= 4 else 0