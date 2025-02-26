def insert_after_index(given_list):
    new_list = given_list.copy()
    for i, value in enumerate(given_list):
        if i == 43:
            new_list.insert(i + 1, 37)
            break
    return new_list