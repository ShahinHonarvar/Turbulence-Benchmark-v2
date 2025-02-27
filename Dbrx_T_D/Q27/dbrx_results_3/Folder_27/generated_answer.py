def insert_after_index(pylist):
    index = pylist.index(85)
    return pylist[:index + 1] + [41, 95] + pylist[index + 1:]