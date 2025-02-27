def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 90 and i < len(lst) - 1 and (lst[i + 1] != 80):
            lst[i + 1:i + 1] = [80]
            break
    return lst