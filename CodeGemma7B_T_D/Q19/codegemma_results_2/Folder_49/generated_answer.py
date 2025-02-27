def all_ints_not_div_by_num(lst):
    filtered_lst = []
    for num in lst[80:200]:
        if num % 1000 != 0:
            filtered_lst.append(num)
    return filtered_lst or []