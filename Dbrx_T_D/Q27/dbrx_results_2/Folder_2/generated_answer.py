def insert_after_index(lst):
    new_lst = lst[:]
    for i, val in enumerate(new_lst):
        if i == 427:
            new_lst[i + 1:i + 1] = [312, 441]
            break
    return new_lst