def find_second_largest_num(numbers):
    sub_list = numbers[35:50]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort(reverse=True)
        return sub_list[1]