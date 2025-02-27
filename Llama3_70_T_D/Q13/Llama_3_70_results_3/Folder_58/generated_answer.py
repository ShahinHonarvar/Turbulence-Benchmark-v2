def find_second_largest_num(numbers):
    sub_list = numbers[209:557]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list, reverse=True)[1]