def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = numbers[12:93]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list), reverse=True)[1]