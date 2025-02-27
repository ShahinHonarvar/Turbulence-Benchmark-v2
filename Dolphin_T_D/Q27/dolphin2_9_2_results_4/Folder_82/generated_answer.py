def insert_after_index(lst):
    cnt = 0
    for i in lst:
        cnt += 1
        if cnt == 84:
            lst.insert(cnt + 1, 771.92)
            return lst
    return lst