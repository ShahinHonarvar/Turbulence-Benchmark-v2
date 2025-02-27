def insert_after_index(lst):
    new_lst = []
    inserted = False
    for num in lst:
        new_lst.append(num)
        if num == 693 and (not inserted):
            new_lst.extend([606, 873])
            inserted = True
    return new_lst