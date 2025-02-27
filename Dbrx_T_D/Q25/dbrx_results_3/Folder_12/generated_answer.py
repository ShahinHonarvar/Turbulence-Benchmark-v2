def insert_at_index(lst):
    new_lst = [0] * (len(lst) + 1)
    for i in range(len(lst)):
        if i < 57:
            new_lst[i] = lst[i]
        else:
            new_lst[i + 1] = lst[i]
    new_lst[57] = 96
    return new_lst