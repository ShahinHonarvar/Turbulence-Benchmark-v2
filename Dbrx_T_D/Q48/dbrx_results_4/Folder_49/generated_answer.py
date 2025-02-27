def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[80], int_tuple[200])
    missing_sum = sum(set(range(a + 1, b)) - set(int_tuple[80:201]))
    if missing_sum % 2:
        return bin(missing_sum).split('0b')[1]
    else:
        return hex(missing_sum).split('0x')[1].upper()