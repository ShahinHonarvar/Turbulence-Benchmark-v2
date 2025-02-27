def insert_after_index(arr):
    for i, item in enumerate(arr):
        if i == 323:
            arr.insert(i + 1, [389, 303])
            break
    return arr