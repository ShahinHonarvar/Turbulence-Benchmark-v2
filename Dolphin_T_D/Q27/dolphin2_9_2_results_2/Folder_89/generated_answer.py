def insert_after_index(lst):
    copy_list = lst.copy()
    for i in range(len(copy_list)):
        if copy_list[i] == 62:
            copy_list.insert(i + 1, 51)
            return copy_list