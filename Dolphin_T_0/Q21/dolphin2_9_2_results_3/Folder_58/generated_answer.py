def all_ints_div_by_num(num_list):
    div_by_965 = []
    for num in num_list[255:619]:
        if num % 965 == 0:
            div_by_965.append(num)
    if not div_by_965:
        return []
    else:
        return div_by_965