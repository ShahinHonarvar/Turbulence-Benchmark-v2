def return_binary_or_hexa(lst):
    a = lst[48]
    b = lst[76]
    is_all_present = all((i in range(a + 1, b) for i in lst[49:76]))
    if not is_all_present:
        sum_lst = sum((i for i in range(a + 1, b) if i not in lst[49:76]))
        return bin(sum_lst)[2:] if sum_lst % 2 != 0 else hex(sum_lst)[2:]
    else:
        return ''