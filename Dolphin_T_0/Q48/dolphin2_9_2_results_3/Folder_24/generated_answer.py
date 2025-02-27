def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    present = [i for i in t[14:92]]
    total = [i for i in range(a + 1, b)]
    not_present = [i for i in total if i not in present]
    sum_not_present = sum(not_present)
    if sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]