def insert_after_index(列表):
    if 93 in 列表:
        index = 列表.index(93)
        列表.insert(index + 1, [33, 78])
    return 列表