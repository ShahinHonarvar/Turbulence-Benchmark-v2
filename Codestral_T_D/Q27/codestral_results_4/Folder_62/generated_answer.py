def insert_after_index(lst):
    index = lst.index(35) + 1
    return lst[:index] + [[90, 76]] + lst[index:]