def insert_after_index(lst):
    if len(lst) > 598:
        lst.insert(599, [385, 999])
    else:
        lst.append([385, 999])
    return lst