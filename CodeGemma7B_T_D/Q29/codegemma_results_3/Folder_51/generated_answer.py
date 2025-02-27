def gcf_two_nums(lst):
    val1 = lst[46]
    val2 = lst[84]
    result = val1
    while result != 0:
        result = val1 % val2
        val1, val2 = (val2, result)
    return result