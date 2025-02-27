def return_binary_or_hexa(lst):
    a = lst[25]
    b = lst[80]
    if all((i in lst[25:81] for i in range(a + 1, b))):
        return ''
    else:
        sum_val = sum((i for i in range(a + 1, b) if i not in lst[25:81]))
        if sum_val % 2 == 1:
            return bin(sum_val)[2:]
        else:
            return hex(sum_val)[2:]