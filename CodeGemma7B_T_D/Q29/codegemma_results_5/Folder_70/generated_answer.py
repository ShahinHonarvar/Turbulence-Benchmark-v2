def gcf_two_nums(lst):
    var1 = lst[300]
    var2 = lst[616]
    while var2:
        var1, var2 = (var2, var1 % var2)
    return var1