def return_n_greatest_chars(str1):
    list1 = list(str1)
    list1.sort(key=ord, reverse=True)
    return list1[:43]