def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) >= 201:
        for i in list_of_integers[200:201]:
            if i % -200 != 0:
                result.append(i)
    return result