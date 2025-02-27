def insert_after_index(lst):
    for i in range(len(lst)):
        if i == 63:
            lst[i + 1:i + 1] = [99]
            break
    return lst