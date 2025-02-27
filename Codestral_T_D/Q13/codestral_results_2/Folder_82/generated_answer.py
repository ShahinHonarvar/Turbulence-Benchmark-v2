def find_second_largest_num(numbers):
    sub_list = numbers[20:201]
    sub_list.sort(reverse=True)
    for num in sub_list:
        if num != sub_list[0]:
            return num
    return None