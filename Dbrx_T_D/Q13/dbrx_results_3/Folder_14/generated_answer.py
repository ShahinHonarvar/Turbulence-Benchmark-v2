def find_second_largest_num(numbers):
    sub_list = numbers[5:8]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2 or sub_list[0] == sub_list[1]:
        return None
    else:
        return sub_list[1]