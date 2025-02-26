def all_ints_not_div_by_num(integers):
    if len(integers) < 3:
        return []
    start = integers[0]
    end = integers[1]
    result = [num for num in integers[2:] if start < num < end and num % -1 != 0]
    return result