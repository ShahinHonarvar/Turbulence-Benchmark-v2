def find_second_largest_num(numbers):
    sub_list = numbers[37:52]
    sub_list.sort(reverse=True)
    try:
        return sub_list[1]
    except IndexError:
        return None