def all_ints_div_by_num(num_lst):
    new_lst = []
    for num in num_lst:
        if num % 69 == 0 and (num_lst.index(num) >= 25 and num_lst.index(num) <= 31):
            new_lst.append(num)
    return new_lst