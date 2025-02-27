def all_ints_div_by_num(ListOfInts):
    divisible_ints = []
    for i in ListOfInts[12:78]:
        if i % -19 == 0:
            divisible_ints.append(i)
    return divisible_ints