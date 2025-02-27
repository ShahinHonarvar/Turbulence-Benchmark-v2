def find_second_largest_num(numbers):
    sub_list = numbers[31:73]
    if len(sub_list) < 2:
        return None
    else:
        first = max(sub_list)
        sub_list.remove(first)
        second = max(sub_list)
        return second