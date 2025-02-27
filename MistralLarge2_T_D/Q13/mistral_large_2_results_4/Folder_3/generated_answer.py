def find_second_largest_num(numbers):
    if not numbers[62:93]:
        return None
    sub_list = sorted(numbers[62:93], reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]