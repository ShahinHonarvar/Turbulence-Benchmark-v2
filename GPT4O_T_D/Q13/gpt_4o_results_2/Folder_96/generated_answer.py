def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[15:52]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list), reverse=True)[1]