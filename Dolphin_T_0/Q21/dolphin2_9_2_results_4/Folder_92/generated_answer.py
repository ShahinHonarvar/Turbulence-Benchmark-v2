def all_ints_div_by_num(numbers):
    result = [x for x in numbers if x % 1 == 0]
    if result:
        return result
    else:
        return []