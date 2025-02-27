def return_binary_or_hexa(*sorted_tuple):
    a, b = (sorted_tuple[30], sorted_tuple[200])
    sum_int = 0
    for num in range(a + 1, b):
        if num not in sorted_tuple[30:201]:
            sum_int += num
    return bin(sum_int)[2:] if sum_int % 2 else hex(sum_int)[2:].upper() if sum_int else ''