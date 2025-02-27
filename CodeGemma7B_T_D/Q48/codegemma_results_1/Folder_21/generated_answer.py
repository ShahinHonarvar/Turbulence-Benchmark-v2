def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[15]
    b = sorted_tuple[57]
    sum_missing_int = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[15:58]:
            sum_missing_int += i
    return bin(sum_missing_int)[2:] if sum_missing_int % 2 else hex(sum_missing_int)[2:].lower()