def insert_after_index(data):
    for i in range(len(data)):
        if data[i] == 761:
            data.insert(i + 1, 925)
            return data
    return data