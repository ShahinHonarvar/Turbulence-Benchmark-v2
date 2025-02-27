def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sub_list = numbers[8:10]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[0]