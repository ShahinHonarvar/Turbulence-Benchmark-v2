def insert_after_index(lst):
    new_lst = []
    for i in range(len(lst) + 1):
        if i > 62:
            new_lst.append(lst[i - 1])
        elif i == 63:
            new_lst.append(51)
        else:
            new_lst.append(lst[i])
    return new_lst