def find_second_largest_num(lst):
    try:
        temp = lst[90:]
        temp.sort(reverse=True)
        return temp[1]
    except IndexError:
        return None