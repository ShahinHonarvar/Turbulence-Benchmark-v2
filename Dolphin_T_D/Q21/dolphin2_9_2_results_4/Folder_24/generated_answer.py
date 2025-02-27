def all_ints_div_by_num(data):
    if len(data) < 78:
        return []
    result = [num for num in data[12:78] if num % -19 == 0]
    return result