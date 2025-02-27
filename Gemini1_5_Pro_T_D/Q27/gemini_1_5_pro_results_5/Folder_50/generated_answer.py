def insert_after_index(l: list) -> list:
    k = l.index(52) + 1
    return l[0:k] + [38] + l[k:]