def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = sorted(numbers[62:100], reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]