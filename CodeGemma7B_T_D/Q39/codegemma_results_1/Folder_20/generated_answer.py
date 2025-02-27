def return_n_greatest_chars(string):
    list = sorted(string, key=ord)
    list = list[len(list) - 40:len(list)]
    return list