def insert_after_index(lst):
    index = len(lst)
    for i in range(len(lst)):
        if lst[i] == 99:
            index = i
            break
    result = lst[:index + 1] + [99] + lst[index + 1:]
    return result