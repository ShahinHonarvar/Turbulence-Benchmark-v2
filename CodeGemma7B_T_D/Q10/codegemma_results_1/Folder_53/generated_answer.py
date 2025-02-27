def all_odd_ints_exclusive(list):
    list_answer = []
    for i in list:
        if i % 2 != 0 and i > 100 and (i < 101):
            list_answer.append(i)
    return list_answer