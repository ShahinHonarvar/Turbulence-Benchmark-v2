def return_binary_or_hexa(lst):
    a = lst[933]
    b = lst[996]
    sum_lst = [num for num in range(a + 1, b) if num not in lst[933:996]]
    total = sum(sum_lst)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()