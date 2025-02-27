def find_second_largest_num(lst):
    new_lst = lst[66:94]
    new_lst.sort(reverse=True)
    for num in new_lst:
        if new_lst.count(num) > 1:
            new_lst.remove(num)
        if len(new_lst) == 2:
            return new_lst[1]
    return None