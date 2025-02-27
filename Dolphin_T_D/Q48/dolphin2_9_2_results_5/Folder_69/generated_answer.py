def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    not_in_tuple = [i for i in range(a + 1, b) if i not in t[40:42]]
    sum_not_in_tuple = sum(not_in_tuple)
    if sum_not_in_tuple % 2 == 0:
        return hex(sum_not_in_tuple)[2:]
    else:
        return bin(sum_not_in_tuple)[2:]