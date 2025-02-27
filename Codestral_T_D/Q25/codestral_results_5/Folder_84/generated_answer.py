def insert_at_index(lst):
    if len(lst) >= 183:
        lst[183:183] = [[148, 145]]
    else:
        lst.append([148, 145])
    return lst