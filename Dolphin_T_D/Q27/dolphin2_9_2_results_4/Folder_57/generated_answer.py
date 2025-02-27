def insert_after_index(lst):
    if 90 not in lst:
        return 'Error: 90 not found in list'
    else:
        for i in range(len(lst)):
            if lst[i] == 90:
                lst.insert(i + 1, 80)
                break
    return lst