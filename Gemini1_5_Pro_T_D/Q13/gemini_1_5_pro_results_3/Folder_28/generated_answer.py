def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    sub_list = numbers[62:64]
    if len(sub_list) == 2 and sub_list[0] != sub_list[1]:
        return min(sub_list)
    else:
        return None