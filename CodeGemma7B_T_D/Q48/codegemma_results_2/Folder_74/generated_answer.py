def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[69], int_tuple[97])
    total = 0
    for i in range(a + 1, b):
        if i not in int_tuple[69:98]:
            total += i
    return bin(total)[-1] if total % 2 == 1 else hex(total)[-2:].upper()