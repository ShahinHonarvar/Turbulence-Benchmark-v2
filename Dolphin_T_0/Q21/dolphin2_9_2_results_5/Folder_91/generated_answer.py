def all_ints_div_by_num(numbers):
    result = [x for x in numbers if x % 5 == 0]
    if not result:
        return []
    else:
        return result[0]