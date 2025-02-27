def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[10]
    b = integer_tuple[12]
    present_integers = set(range(a + 1, b))
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_integers))
    if missing_sum % 2:
        return bin(missing_sum).split('0b')[1]
    else:
        return hex(missing_sum).split('0x')[1].upper()