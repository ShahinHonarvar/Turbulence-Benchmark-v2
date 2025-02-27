def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[10], sorted_tuple[12])
    summation = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[10:13]:
            summation += i
    return '0b' + bin(summation)[2:] if summation % 2 else '0x' + hex(summation)[2:].upper()