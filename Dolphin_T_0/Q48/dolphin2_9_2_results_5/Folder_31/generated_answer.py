def return_binary_or_hexa(lst):
    a = lst[33]
    b = lst[78]
    sum_integers = sum((i for i in range(a + 1, b) if i not in lst[33:78]))
    if sum_integers % 2 != 0:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:]