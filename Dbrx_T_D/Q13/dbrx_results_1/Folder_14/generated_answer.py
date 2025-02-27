def find_second_largest_num(numbers):
    sub_list = numbers[5:8]
    unique_sub_list = list(set(sub_list))
    unique_sub_list.sort(reverse=True)
    if len(unique_sub_list) < 2:
        return None
    else:
        return unique_sub_list[1]