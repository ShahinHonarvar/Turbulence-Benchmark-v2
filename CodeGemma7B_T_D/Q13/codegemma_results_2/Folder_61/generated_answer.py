def find_second_largest_num(list_num):
    list_num.sort(reverse=True)
    try:
        return list_num[7]
    except IndexError:
        return 'None'