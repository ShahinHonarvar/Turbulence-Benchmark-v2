def insert_after_index(l):
    index_to_insert = 60
    element_to_insert = [80, 74]
    return l[:index_to_insert + 1] + element_to_insert + l[index_to_insert + 1:]