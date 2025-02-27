def find_second_largest_num(lst):
    var1 = lst[30:88]
    var1.sort()
    if len(var1) < 2:
        return None
    else:
        return var1[-2]