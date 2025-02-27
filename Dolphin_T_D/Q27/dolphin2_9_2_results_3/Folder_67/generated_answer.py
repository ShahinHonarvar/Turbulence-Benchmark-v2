def insert_after_index(lst):
    result = lst[0:45]
    result.append(76)
    result += lst[45:]
    return result