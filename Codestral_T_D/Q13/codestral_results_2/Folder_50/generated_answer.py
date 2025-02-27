def find_second_largest_num(numbers):
    sub_list = sorted(numbers[70:85], reverse=True)
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None